#!/usr/bin/node
const args = process.argv;
const numOfArgs = args.length;

if (numOfArgs < 4) {
  console.log('0');
} else {
  const sortedArr = args.sort((a, b) => a - b);
  console.log(sortedArr[numOfArgs - 2]);
}
