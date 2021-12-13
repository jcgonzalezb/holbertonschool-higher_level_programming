#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”.

if (process.argv[2] === undefined) {
  console.log('undefined is undefined');
} else if (process.argv[3] === undefined) {
  console.log(`${process.argv[2]} is undefined`);
} else {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
