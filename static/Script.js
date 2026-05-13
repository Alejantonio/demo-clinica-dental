// Seleccionamos los elementos del interruptor
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const themeText = document.getElementById('theme-text');

// Verificamos que el interruptor exista
if (themeToggle) {
    themeToggle.addEventListener('change', () => {
        // Alternamos la clase en el body
        document.body.classList.toggle('light-mode');
        
        // Cambiamos el texto y el emoji
        if(themeToggle.checked) {
            themeIcon.textContent = '☀️';
            themeText.textContent = 'Modo claro';
        } else {
            themeIcon.textContent = '🌙';
            themeText.textContent = 'Modo oscuro';
        }
    });
}

// 1. FUNCIÓN PARA APLICAR EL TEMA
function aplicarTema(modo) {
    if (modo === 'light') {
        document.body.classList.add('light-mode');
        if (themeToggle) themeToggle.checked = true;
        if (themeIcon) themeIcon.textContent = '☀️';
        if (themeText) themeText.textContent = 'Modo claro';
    } else {
        document.body.classList.remove('light-mode');
        if (themeToggle) themeToggle.checked = false;
        if (themeIcon) themeIcon.textContent = '🌙';
        if (themeText) themeText.textContent = 'Modo oscuro';
    }
}

// 2. LÓGICA DE INICIO (Prioridad: Memoria > Hora)
function inicializarInterfaz() {
    const preferenciaGuardada = localStorage.getItem('tema-usuario');

    if (preferenciaGuardada) {
        // Si el usuario ya hizo clic antes, usamos eso
        aplicarTema(preferenciaGuardada);
    } else {
        // Si es nuevo, usamos la hora
        const hora = new Date().getHours();
        const esDia = hora >= 6 && hora < 18;
        aplicarTema(esDia ? 'light' : 'dark');
    }
}

// 3. EVENTO DEL BOTÓN (Guardar la elección)
if (themeToggle) {
    themeToggle.addEventListener('change', () => {
        const nuevoModo = themeToggle.checked ? 'light' : 'dark';
        aplicarTema(nuevoModo);
        // Guardamos la elección en la memoria del navegador
        localStorage.setItem('tema-usuario', nuevoModo);
    });
}

// Ejecutar al cargar
window.onload = inicializarInterfaz;

// 1. FUNCIÓN PARA APLICAR EL TEMA
function aplicarTema(modo) {
    if (modo === 'light') {
        document.body.classList.add('light-mode');
        if (themeToggle) themeToggle.checked = true;
        if (themeIcon) themeIcon.textContent = '☀️';
        if (themeText) themeText.textContent = 'Modo claro';
    } else {
        document.body.classList.remove('light-mode');
        if (themeToggle) themeToggle.checked = false;
        if (themeIcon) themeIcon.textContent = '🌙';
        if (themeText) themeText.textContent = 'Modo oscuro';
    }
}

// 2. LÓGICA DE INICIO (Prioridad: Memoria > Hora)
function inicializarInterfaz() {
    const preferenciaGuardada = localStorage.getItem('tema-usuario');

    if (preferenciaGuardada) {
        // Si el usuario ya hizo clic antes, usamos eso
        aplicarTema(preferenciaGuardada);
    } else {
        // Si es nuevo, usamos la hora
        const hora = new Date().getHours();
        const esDia = hora >= 6 && hora < 18;
        aplicarTema(esDia ? 'light' : 'dark');
    }
}

// 3. EVENTO DEL BOTÓN (Guardar la elección)
if (themeToggle) {
    themeToggle.addEventListener('change', () => {
        const nuevoModo = themeToggle.checked ? 'light' : 'dark';
        aplicarTema(nuevoModo);
        // Guardamos la elección en la memoria del navegador
        localStorage.setItem('tema-usuario', nuevoModo);
    });
}

let slideIndex = 1;
showSlides(slideIndex);

// Control de siguiente/anterior
function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide");
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex-1].style.display = "block";  
}

// Cambio automático cada 5 segundos
setInterval(() => {
    plusSlides(1);
}, 5000);

// Ejecutar al cargar
window.onload = inicializarInterfaz;