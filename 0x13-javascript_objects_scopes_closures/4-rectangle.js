#!/usr/bin/node
// Write a class Rectangle that defines a rectangle.

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    for (i = 0; i < this.height; i++) {
      let temp = '';
      for (j = 0; j < this.width; j++) {
        temp = temp + '' + 'X';
      }
      console.log(temp);
    }
  }

  rotate () {
    let i = 0;
    let j = 0;
    for (i = 0; i < this.width; i++) {
      let temp = '';
      for (j = 0; j < this.height; j++) {
        temp = temp + '' + 'X';
      }
      console.log(temp);
    }
  }

  double () {
    let i = 0;
    let j = 0;
    for (i = 0; i < this.height * 2; i++) {
      let temp = '';
      for (j = 0; j < this.width * 2; j++) {
        temp = temp + '' + 'X';
      }
      console.log(temp);
    }
  }
};
