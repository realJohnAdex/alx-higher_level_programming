// Make a GET request to the API URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Get the movie titles from the response data
    var movieTitles = data.results.map(function(movie) {
        return movie.title;
    });

    // Create a new unordered list element
    var ul = $('<ul id="list_movies"></ul>');

    // Append each movie title as a list item to the unordered list
    movieTitles.forEach(function(title) {
        var li = $('<li></li>').text(title);
        ul.append(li);
    });

    // Append the unordered list to the body of the HTML document
    $('body').append(ul);
});
