let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
let drawing = false;

// Gestion du dessin sur le canvas
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mousemove', draw);

function startDrawing(e) {
    drawing = true;
    draw(e);
}

function stopDrawing() {
    drawing = false;
    ctx.beginPath();
}

function draw(e) {
    if (!drawing) return;
    ctx.lineWidth = 10;
    ctx.lineCap = 'round';
    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

// Effacer le canvas
document.getElementById('clearButton').addEventListener('click', function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

// Envoi de l'image pour la prédiction
document.getElementById('predictButton').addEventListener('click', function() {
    let image = canvas.toDataURL('image/png');
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({image: image})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = 'Prédiction: ' + data.prediction;
    });
});
