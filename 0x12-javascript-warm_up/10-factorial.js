#!/usr/bin/node

function factorial (num) {
  num = parseInt(num);
  if (num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const args = process.argv;
const num1 = args[2];
const res = factorial(num1);
console.log(res);
