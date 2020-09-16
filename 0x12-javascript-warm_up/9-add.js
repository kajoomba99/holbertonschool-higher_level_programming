#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const args = process.argv;
const num1 = args[2];
const num2 = args[3];

console.log(add(num1, num2));
