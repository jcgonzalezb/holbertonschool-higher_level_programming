#!/usr/bin/node
// Write a function that returns the reversed version of a list.

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  while (i < j) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    i++;
    j--;
  }
  return list;
};
