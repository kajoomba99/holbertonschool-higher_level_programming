#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request
  .get(url)
  .on('response', response => console.log('code:', response.statusCode));
