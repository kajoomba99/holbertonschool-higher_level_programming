#!/usr/bin/node
const numOfArgs = process.argv.length;

const pluralize = (long) => {
  if (long === 1) {
    return '';
  } else {
    return 's';
  }
};

if (numOfArgs <= 2) {
  console.log('No argument');
} else {
  console.log('Argument' + pluralize(numOfArgs - 2) + ' found');
}
