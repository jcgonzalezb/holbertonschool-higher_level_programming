#!/usr/bin/node
// Write a script that that writes a string to a file.

const fs = require('fs');

const data = process.argv[3];

fs.writeFile(process.argv[2], '\ufeff' + data, (err) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
