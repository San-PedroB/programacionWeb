


//Validacion de los input del formulario

// Función para validar solo letras y espacios
function validarNombre(nombre) {
    const caracteresPermitidos = /^[a-zA-Z\s]+$/;
    return caracteresPermitidos.test(nombre.trim());
}

// Función para validar teléfono
function validarTelefono(telefono) {
    const caracteresPermitidos = /^\d{9}$/;
    return caracteresPermitidos.test(telefono.trim());
}

// Función para validar largo minimo del mensaje
function validarMensaje(mensaje) {
    return mensaje.trim().length >= 10;
}

function validarCorreo(correo) {
    return correo.include("@")
}

document.querySelector('.form-contact').addEventListener('submit', function(event) {
    let valid = true;

    const nameInput = document.getElementById('name-input');
    const lastnameInput = document.getElementById('lastname-input');
    const phoneInput = document.getElementById('phone-input');
    const emailInput = document.getElementById('email-input');
    const messageInput = document.getElementById('message-input');

    // Llamadas a las funciones de validación con los valores de los campos
    if (!validarNombre(nameInput.value)) {
        alert('Por favor, escribe un nombre válido (solo letras).');
        valid = false;
    }

    if (!validarNombre(lastnameInput.value)) {
        alert('Por favor, escribe apellidos válidos (solo letras).');
        valid = false;
    }

    if (!validarTelefono(phoneInput.value)) {
        alert('Por favor, escribe un número de teléfono válido con 9 dígitos.');
        valid = false;
    }

    if (!emailInput()) {
        alert('Por favor, escribe un correo electrónico válido.');
        valid = false;
    }

    if (!validarMensaje(messageInput.value)) {
        alert('Por favor, escribe un mensaje de al menos 10 caracteres.');
        valid = false;
    }

    if (!validarCorreo(emailInput.value)){
        alert('Por favor, escribe un correo valido');
        valid = false;
    }

    if (!valid) {
        event.preventDefault();
    }

});

function initMap() {
    const location = { lat: -33.494722354604036, lng: -70.72356904981942 }; // Coordenadas 
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: location
    });
        new google.maps.Marker({
        position: location,
        map: map
    });
}

document.addEventListener('DOMContentLoaded', function() {
    initMap();
});

var carrito = [];

localStorage.setItem("carrito", JSON.stringify(carrito));