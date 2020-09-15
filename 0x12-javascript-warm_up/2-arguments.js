#!/usr/bin/node
const numOfArgs = process.argv.length;

if (numOfArgs > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
