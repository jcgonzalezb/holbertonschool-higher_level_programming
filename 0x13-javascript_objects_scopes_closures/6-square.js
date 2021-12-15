#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square.

const OriginalSquare = require('./5-square');

module.exports = class Square extends OriginalSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      let j = 0;
      for (i = 0; i < this.width; i++) {
        let temp = '';
        for (j = 0; j < this.height; j++) {
          temp = temp + '' + 'C';
        }
        console.log(temp);
      }
    }
  }
};
