// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header. Must use the JQuery API.

$(document).ready(function () {
  $('div').on({
    click: function () {
      $(this).css('color', 'red');
    }
  });
});
