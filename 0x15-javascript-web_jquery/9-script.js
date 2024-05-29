// Import jQuery from a CDN
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
script.integrity = 'sha384-KyZXEAg3Q4zv3+Vn+I3+ZBz2o7gYw6b4zjv9+Xu7z3q0Y1ZJz4ZJ3w8X5ZJZ1z6y';
script.crossOrigin = 'anonymous';
document.head.appendChild(script);

// Wait for jQuery to be loaded
script.onload = function() {
    // Fetch the translation from the given URL
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Display the translation in the HTML tag DIV#hello
        $('#hello').text(data.hello);
    });
};
