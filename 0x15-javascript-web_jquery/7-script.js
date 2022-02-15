// Write a JavaScript script that fetches the character name from a URL.

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (data) {
    $('div').text(data.name);
  }
});
