#!/usr/bin/node
module.export = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}
