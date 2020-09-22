#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const path = args[3];
request(url, (err, resp, body) => {
  if (err) return console.error(err);
  fs.writeFile(path, body, 'utf8', err => {
    if (err) return console.log(err);
  });
});
