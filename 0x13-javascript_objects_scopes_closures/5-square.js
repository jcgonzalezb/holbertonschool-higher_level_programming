#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle.

class Rectangle {
  constructor (w, h) {
    this.name = 'Rectangle';
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.name = 'Square';
    if (size > 0) {
      this.size = size;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    for (i = 0; i < this.size; i++) {
      let temp = '';
      for (j = 0; j < this.size; j++) {
        temp = temp + '' + 'X';
      }
      console.log(temp);
    }
  }

  double () {
    this.size *= 2;
  }
};
