// Write a JavaScript script that fetches from URL and displays the value of hello from that fetch in the HTML tag DIV#hello.

$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (data) {
    $('DIV#hello').text(data.hello);
  }
});
