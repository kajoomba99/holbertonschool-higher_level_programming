#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (character = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(character.repeat(this.size));
    }
  }
};
