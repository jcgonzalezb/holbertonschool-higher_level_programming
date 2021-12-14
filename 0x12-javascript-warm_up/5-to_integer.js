#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (parseInt(process.argv[2])) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
