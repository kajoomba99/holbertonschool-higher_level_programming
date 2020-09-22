#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const filename = args[2];
const text = args[3];
fs.writeFile(filename, text, 'utf8', err => {
  if (err) return console.log(err);
});
