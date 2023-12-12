#!/usr/bin/node
// Defining constants
const myConst = 'undefined';

// Printing outputs
if (process.argv[2] && process.argv[3]) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else if (process.argv[2] && !process.argv[3]) {
  console.log(`${process.argv[2]} is ${myConst}`);
} else {
  console.log(`${myConst} is ${myConst}`);
}
