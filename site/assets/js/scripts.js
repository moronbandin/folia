document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([42.5751, -8.1339], 8);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Añadir marcadores desde los datos
    var markers = [
        // Agrega aquí tus marcadores con coordenadas y enlaces
        {"coords": [42.858, -8.544], "title": "Muiñeira de Bembibre", "url": "/pezas/muinheiras/pezas/bembibre.md"},
        // Más marcadores...
    ];

    markers.forEach(function(marker) {
        L.marker(marker.coords).addTo(map)
            .bindPopup(`<a href="${marker.url}">${marker.title}</a>`);
    });
});
