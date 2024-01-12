from flask import Flask, render_template, request, jsonify, redirect
import pandas as pd
import numpy as np
from PIL import Image
from utils import fetch_company_news, create_stock_graph
from models import User, db
import base64
import io
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import joblib

# Prédictions
digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
joblib.dump(clf, 'mnist_model.pkl')
model = joblib.load('mnist_model.pkl')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Création des tables non existantes
with app.app_context():
    db.create_all()

# Dataset
df = pd.read_excel('data/tesla_apple.xlsx')

# Route accueil
@app.route("/")
def hello():
    return render_template("home.html")

# Route JMS
@app.route("/jms")
def jms():
    return render_template("the_james_mind.html")

# Route formulaire d'utilisateurs
@app.route('/envoi-infos', methods=['GET', 'POST'])
def envoi_infos():
    if request.method == 'POST':
        prenom = request.form['prénom']
        nom = request.form['nom']
        sexe = request.form['sexe']
        pseudo = request.form['pseudo']

        user_exists = User.query.filter_by(pseudo=pseudo).first()
        if user_exists:
            return "Ce pseudo existe déjà. Veuillez en choisir un autre."

        new_user = User(prenom=prenom, nom=nom, sexe=sexe, pseudo=pseudo)
        db.session.add(new_user)
        db.session.commit()

        titre = "Mme" if sexe == "F" else "Mr"
        message = f"Bonjour {titre} {prenom} {nom}, votre nom d'utilisateur est {pseudo}"
        return render_template("bienvenue.html", message=message)

    return render_template('formulaire.html')

# Route utilisateurs inscrits
@app.route('/utilisateurs-inscrits')
def utilisateurs_inscrits():
    users = User.query.all()
    return render_template('utilisateurs_inscrits.html', users=users)

# Route upload dataset
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename != '':
            if '.csv' in uploaded_file.filename:
                df = pd.read_csv(uploaded_file)
            elif '.xlsx' in uploaded_file.filename:
                df = pd.read_excel(uploaded_file)

            stats_html = df.describe().to_html()
            stats_html_clean = stats_html.strip("[' ]")

            return render_template('stats.html', tables=stats_html_clean)
    return render_template('upload.html')


# Route formulaire de news
@app.route('/get-news-form', methods=['GET', 'POST'])
def get_news_form():
    if request.method == 'POST':
        company = request.form['company']
        news_data = fetch_company_news(company)
        if news_data:
            return render_template("news.html", news=news_data, company=company)
        else:
            return f"Pas de nouvelles disponibles pour {company}."
    return render_template('get_news_form.html')



# Route statistiques
@app.route("/stats")
def stats():
    return render_template("stats.html")

# Route graphiques
@app.route('/stock_graph')
def stock_graph():
    apple_graph_html = create_stock_graph(df, 'APPLE')
    tesla_graph_html = create_stock_graph(df, 'TESLA')
    return render_template('stock_graph.html', apple_graph_html=apple_graph_html, tesla_graph_html=tesla_graph_html)

# Route prédictions MNIST
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    prediction_result = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            image = Image.open(file.stream).convert('L')
            image = image.resize((8, 8), Image.Resampling.LANCZOS)
            image = np.array(image)
            image = image.reshape(1, -1)
            prediction_result = model.predict(image)[0]

    return render_template('prediction.html', prediction=prediction_result)

# Route prédiction dessin
@app.route('/predict', methods=['POST'])
def prediction_dessin():
    data = request.get_json()
    if data and 'image' in data:
        image_base64 = data['image']
        image_data = base64.b64decode(image_base64.split(',')[1])
        image = Image.open(io.BytesIO(image_data)).convert('L')
        image = image.resize((8, 8), Image.Resampling.LANCZOS)

        image_array = np.array(image).reshape(1, -1)

        prediction = model.predict(image_array)[0]

        return jsonify({'prediction': int(prediction)})
    else:
        return 'Données non reçues', 400

if __name__ == '__main__':
    app.run(debug=True)
