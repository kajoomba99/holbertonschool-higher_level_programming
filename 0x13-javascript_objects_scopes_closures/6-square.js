#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (character = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
};
