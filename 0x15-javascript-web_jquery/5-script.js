const mylist = $('.my_list');
$('#add_item').click(() => {
  mylist.append('<li>Item</li>');
});
