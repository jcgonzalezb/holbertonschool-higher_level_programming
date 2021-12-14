#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

function print2largest (arr, arr_size) {
  let i;

  if (arr_size < 2) {
    console.log('0');
    return;
  }
  arr.sort();

  for (i = arr_size - 2; i >= 0; i--) {
    if (arr[i] !== arr[arr_size - 1]) {
      console.log(arr[i]);
      return;
    }
  }
  console.log('0');
}

const arr = process.argv;
const n = process.argv.length;
print2largest(arr, n);
