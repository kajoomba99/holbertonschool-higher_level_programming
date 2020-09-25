$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', data => {
    const hello = data.hello;
    $('#hello').text(hello);
  });
});
