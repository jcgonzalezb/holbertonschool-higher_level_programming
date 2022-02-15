#!/usr/bin/node
// Write a JavaScript script that fetches from URL and  and displays the value of hello from that fetch in the HTML tag DIV#hello.

$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (data) {
    const films = data.results;
    $.each(films, function (i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
