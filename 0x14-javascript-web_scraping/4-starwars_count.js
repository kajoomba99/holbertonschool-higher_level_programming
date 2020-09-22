#!/usr/bin/node
const request = require('request');
let wedge = 0;
const args = process.argv;
const url = args[2];
request(url, (err, resp, body) => {
  if (err) return console.log(err);
  const jsonResp = JSON.parse(body);
  const { results } = jsonResp;
  for (let i = 0; i < results.length; i++) {
    const item = results[i];
    const characters = item.characters;
    if (characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      wedge += 1;
    }
  }
  console.log(wedge);
});
