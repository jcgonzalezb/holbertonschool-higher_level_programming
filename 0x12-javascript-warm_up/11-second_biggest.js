#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const arr = process.argv;
const n = process.argv.length;

function print2largest (arr, n) {
  let i;
  let largest = -2454635434;
  let second = -2454635434;

  if (n < 2) {
    console.log('0');
    return;
  }

  for (i = 0; i < n; i++) {
    if (arr[i] > largest) {
      second = largest;
      largest = arr[i];
    } else if (arr[i] !== largest && arr[i] > second) {
      second = arr[i];
    }
  }

  if (second === -2454635434) {
    console.log('0');
  } else {
    console.log(second);
  }
}

print2largest(arr, n);
