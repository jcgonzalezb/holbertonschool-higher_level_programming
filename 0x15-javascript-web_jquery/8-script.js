// Write a JavaScript script that fetches and lists the title for all movies by using a URL.

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (data) {
    const films = data.results;
    $.each(films, function (i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
