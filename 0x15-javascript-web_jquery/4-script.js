#!/usr/bin/node
// Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header.
$(document).ready(function () {
  $('div').on({
    click: function () {
      $('header').toggleClass('green red');
    }
  });
});
