#!/usr/bin/node
// Write a script that prints the first argument passed to it.

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  for (let i = 2; i < 3; ++i) {
    console.log(`${process.argv[i]}`);
  }
}
