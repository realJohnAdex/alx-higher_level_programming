// This script toggles red and green
$(document).ready(function() {
    $('#toggle_header').click(function() {
        $('header').toggleClass('red green');
    });
});
