#!/usr/bin/node
const args = process.argv;
const numOfArgs = args.length;

if (numOfArgs <= 2 || args[2] === '1') {
  console.log(0);
} else {
  const myArr = args.slice(2, numOfArgs);
  const arrOfInts = myArr.map(item => {
    return parseInt(item);
  });
  const long = arrOfInts.length;
  const sortedArr = arrOfInts.sort((a, b) => a - b);
  const socondLargestNumber = sortedArr[long - 2];
  console.log(socondLargestNumber);
}
