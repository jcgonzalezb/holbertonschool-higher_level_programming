#!/usr/bin/node
// Write a script that prints x times “C is fun”.

const message = 'C is fun';

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2])) {
  let index = 0;
  while (index < parseInt(process.argv[2])) {
    console.log(message);
    index++;
  }
}
