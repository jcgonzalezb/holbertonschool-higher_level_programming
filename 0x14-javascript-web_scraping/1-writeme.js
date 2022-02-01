#!/usr/bin/node
// Write a script that that writes a string to a file.

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
