#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  const derulo = JSON.parse(body);
  let c = 0;
  for (const film of derulo.results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        c++;
      }
    }
  }
  console.log(c);
});
