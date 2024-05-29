import $ from 'jquery';
// Import the jQuery library
// Fetch the character name from the URL
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Display the character name in the HTML tag <div id="character">
    $('#character').text(data.name);
});
