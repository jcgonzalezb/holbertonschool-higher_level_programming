#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const fs = require('fs');
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
