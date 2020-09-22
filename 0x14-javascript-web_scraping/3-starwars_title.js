#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
request(`https://swapi-api.hbtn.io/api/films/${id}`, function (error, response, body) {
  if (error) return console.log(error);
  const jsonResponse = JSON.parse(body);
  const { title } = jsonResponse;
  console.log(title);
});
