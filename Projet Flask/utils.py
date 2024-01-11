import requests
import plotly.express as px
from models import db, Log
import pandas as pd

# fonction API news bourse
def fetch_company_news(company_name):
    url = "https://devapi.ai/api/v1/markets/news"
    headers = {'Authorization': 'Bearer 335|WdhQq7SHdh76ccAAUFDpRooOYI0KCYpeNHRlG5o8'}
    params = {'ticker': 'AAPL,TSLA'}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get("body", [])  # Retourne la liste des nouvelles
        else:
            return []  # Retourne une liste vide si le statut n'est pas 200
    except requests.RequestException as e:
        return []

# fonction recherche log
def log_search(user, datetime, ticker, company, price):
    new_log = Log(user=user, datetime=datetime, ticker=ticker, company=company, price_at_datetime=price)
    db.session.add(new_log)
    db.session.commit()

# fonction graphique des prix des actions
df = pd.read_excel('data/tesla_apple.xlsx')


def create_stock_graph(df, company_name):
    # Filtrer les données pour l'entreprise spécifiée
    filtered_df = df[df['Entreprise'] == company_name]
    # Transformer les données pour avoir les dates en colonne et les prix en ligne
    filtered_df = filtered_df.melt(id_vars=['Entreprise'], var_name='Date', value_name='Prix')
    # Créer le graphique
    fig = px.line(filtered_df, x='Date', y='Prix', title=f'Prix des Actions de {company_name}')
    # Convertir le graphique en HTML
    graph_html = fig.to_html()
    return graph_html