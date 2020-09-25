$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  const results = data.results;
  $.each(results, (index, item) => {
    $('#list_movies').append('<li>' + item.title + '</li>');
  });
});
