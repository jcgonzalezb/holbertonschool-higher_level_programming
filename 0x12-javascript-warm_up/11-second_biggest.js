#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

function print2largest (arr, arr_size) {
  let i;
  largest = second = -2454635434;

  if (arr_size < 2) {
    console.log('0');
    return;
  }

  for (i = 0; i < arr_size; i++) {
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

const arr = process.argv;
const n = process.argv.length;
print2largest(arr, n);
