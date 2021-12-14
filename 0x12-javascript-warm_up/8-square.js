#!/usr/bin/node
// Write a script that prints a square.

let i; let j = 0;

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else if (parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (i = 0; i < size; i++) {
    let temp = '';
    for (j = 0; j < size; j++) {
      temp = temp + '' + 'X';
    }
    console.log(temp);
  }
} else {
  console.log('Missing size');
}
