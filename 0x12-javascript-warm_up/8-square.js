#!/usr/bin/node
const args = process.argv;
if (!args[2] || isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args[2]);
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
