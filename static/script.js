// Corazones flotantes mejorados
function createHearts() {
    const container = document.getElementById('hearts-container');
    const heart = document.createElement('div');
    heart.className = 'heart-msg';
    
    // Usar diferentes emojis de corazón
    const hearts = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🤎', '🖤', '💖', '💗', '💘', '💝'];
    heart.innerHTML = hearts[Math.floor(Math.random() * hearts.length)];
    
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
    heart.style.animationDuration = (Math.random() * 5 + 5) + 's';
    heart.style.animationDelay = (Math.random() * 2) + 's';
    
    container.appendChild(heart);
    
    setTimeout(() => {
        heart.remove();
    }, parseFloat(heart.style.animationDuration) * 1000);
}

// Fotos flotantes (puedes añadir tus URLs de foto)
function createFloatingPhotos() {
    const container = document.getElementById('photos-container');
    const photoUrls = [
        'url("https://ejemplo.com/foto1.jpg")',
        'url("https://ejemplo.com/foto2.jpg")',
        // Añade más URLs de tus fotos
    ];
    
    if (photoUrls.length > 0) {
        const photo = document.createElement('div');
        photo.className = 'photo-msg';
        photo.style.backgroundImage = photoUrls[Math.floor(Math.random() * photoUrls.length)];
        photo.style.left = Math.random() * 100 + 'vw';
        photo.style.top = Math.random() * 100 + 'vh';
        photo.style.animationDuration = (Math.random() * 10 + 10) + 's';
        photo.style.opacity = Math.random() * 0.5 + 0.3;
        
        container.appendChild(photo);
        
        setTimeout(() => {
            photo.remove();
        }, parseFloat(photo.style.animationDuration) * 1000);
    }
}

// Efecto al hacer clic mejorado
document.addEventListener('click', function(e) {
    const clickHeart = document.createElement('div');
    clickHeart.className = 'heart-msg';
    
    const hearts = ['❤️', '💖', '💘', '💝'];
    clickHeart.innerHTML = hearts[Math.floor(Math.random() * hearts.length)];
    
    clickHeart.style.left = (e.clientX - 15) + 'px';
    clickHeart.style.top = (e.clientY - 15) + 'px';
    clickHeart.style.fontSize = '30px';
    clickHeart.style.animationDuration = '2s';
    clickHeart.style.animationName = 'heartBeat';
    
    document.getElementById('hearts-container').appendChild(clickHeart);
    
    setTimeout(() => {
        clickHeart.remove();
    }, 2000);
});

// Navegación entre secciones
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // Remover clase active de todos los botones y secciones
        document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
        
        // Agregar clase active al botón clickeado
        this.classList.add('active');
        
        // Mostrar la sección correspondiente
        const target = this.getAttribute('data-target');
        document.getElementById(target).classList.add('active');
    });
});

// Efecto de carga inicial
document.addEventListener('DOMContentLoaded', function() {
    // Animación de entrada para los elementos
    setTimeout(() => {
        document.querySelector('.love-container').style.opacity = '1';
    }, 100);
    
    // Crear corazones iniciales
    for (let i = 0; i < 15; i++) {
        setTimeout(createHearts, i * 300);
    }
    
    // Crear fotos flotantes
    for (let i = 0; i < 5; i++) {
        setTimeout(createFloatingPhotos, i * 2000);
    }
});

// Crear corazones periódicamente
setInterval(createHearts, 500);
setInterval(createFloatingPhotos, 10000);

// Efecto para las notas completadas
document.querySelectorAll('.task-checkbox input').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const taskTitle = this.closest('.love-task').querySelector('.task-title');
        if (this.checked) {
            taskTitle.classList.add('completed');
        } else {
            taskTitle.classList.remove('completed');
        }
    });
});