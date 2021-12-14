#!/usr/bin/node
// Write a script that computes and prints a factorial.

function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (process.argv[2] === undefined) {
  console.log('1');
} else {
  const fact = factorial(parseInt(process.argv[2]));
  console.log(fact);
}
