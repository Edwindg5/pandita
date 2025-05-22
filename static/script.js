// Crear corazones flotantes
function createHearts() {
    const container = document.getElementById('hearts-container');
    const heart = document.createElement('div');
    heart.className = 'heart-msg';
    heart.innerHTML = '❤️';
    
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
    heart.style.animationDuration = (Math.random() * 3 + 3) + 's';
    
    container.appendChild(heart);
    
    setTimeout(() => {
        heart.remove();
    }, parseFloat(heart.style.animationDuration) * 1000);
}

// Crear corazones periódicamente
setInterval(createHearts, 300);

// Efecto al hacer clic
document.addEventListener('click', function(e) {
    const clickHeart = document.createElement('div');
    clickHeart.className = 'heart-msg';
    clickHeart.innerHTML = '❤️';
    clickHeart.style.left = e.clientX + 'px';
    clickHeart.style.top = e.clientY + 'px';
    clickHeart.style.fontSize = '30px';
    clickHeart.style.animationDuration = '2s';
    
    document.getElementById('hearts-container').appendChild(clickHeart);
    
    setTimeout(() => {
        clickHeart.remove();
    }, 2000);
});