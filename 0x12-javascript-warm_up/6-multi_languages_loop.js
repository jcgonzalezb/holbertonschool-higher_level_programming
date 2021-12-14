#!/usr/bin/node
// Write a script that prints 3 lines using an array of string and a loop.

const messages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let index = 0;

while (index < messages.length) {
  const message = messages[index];
  console.log(message);
  index++;
}
