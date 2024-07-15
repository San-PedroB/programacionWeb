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
    const destination = { lat: -33.494762, lng: -70.723526 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 18,
        center: destination,
    });
    const marker = new google.maps.Marker({
        position: destination,
        map: map,
        title: "Nuestra ubicación",
    });

    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById("directions-panel"));

    document.getElementById("get-directions").addEventListener("click", function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const origin = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                calculateAndDisplayRoute(directionsService, directionsRenderer, origin, destination);
            }, function() {
                alert("Error: La geolocalización falló.");
            });
        } else {
            alert("Error: Tu navegador no soporta la geolocalización.");
        }
    });
}

function calculateAndDisplayRoute(directionsService, directionsRenderer, origin, destination) {
    directionsService.route(
        {
            origin: origin,
            destination: destination,
            travelMode: google.maps.TravelMode.DRIVING,
        },
        (response, status) => {
            if (status === "OK") {
                directionsRenderer.setDirections(response);
            } else {
                window.alert("La solicitud de direcciones falló debido a " + status);
            }
        }
    );
}

// Inicializar el mapa cuando la página haya terminado de cargarse
window.addEventListener('load', function() {
    if (document.getElementById("map")) {
        initMap();
    }
});
