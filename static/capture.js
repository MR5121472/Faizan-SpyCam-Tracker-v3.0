async function getDetails() {
    let ip = await fetch("https://api.ipify.org").then(r => r.text());
    let location = "Unavailable", device = navigator.userAgent;

    try {
        navigator.geolocation.getCurrentPosition(function(position) {
            location = position.coords.latitude + "," + position.coords.longitude;
            sendInfo(ip, location, device);
        }, function() {
            sendInfo(ip, location, device);
        });
    } catch (e) {
        sendInfo(ip, location, device);
    }
}

function sendInfo(ip, location, device) {
    fetch("/info", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ ip, location, device })
    });
}
