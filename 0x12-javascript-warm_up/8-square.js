#!/usr/bin/node
// Write a script that prints x times “C is fun”.


let i; let j = 0;

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else if (parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      console.log('X');
    }
    console.log('');
  }
  } else {
   console.log('Missing size');
}
