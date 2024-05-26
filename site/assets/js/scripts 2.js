document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([42.5751, -8.1339], 8);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add markers or other map features here
});
