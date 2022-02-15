// Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag #add_item.

$(document).ready(function () {
  $('div').on({
    click: function () {
      $('UL.my_list').append('<li>Item</li>');
    }
  });
});
