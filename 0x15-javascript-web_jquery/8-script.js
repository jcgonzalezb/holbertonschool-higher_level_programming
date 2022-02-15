#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all movies by using a URL.

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (data) {
    $('div').text(data.name);
  }
});
