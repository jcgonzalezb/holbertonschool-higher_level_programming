#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square.

const OriginalSquare = require('./5-square');

module.exports = class Square extends OriginalSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
