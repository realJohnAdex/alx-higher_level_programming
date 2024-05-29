// Wait for the document to be ready
$(document).ready(function() {
    // Attach a click event handler to the DIV#red_header element
    $('DIV#red_header').click(function() {
        // Update the text color of the <header> element to red (#FF0000)
        $('header').css('color', '#FF0000');
    });
});
