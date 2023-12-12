#!/usr/bin/node
// Create an array of strings
const myStr = 'C is fun';
const myArg = process.argv[2];

const myInt = parseInt(myArg);
// Use console.log(...) to print the value of myVar
if (!isNaN(myInt)) {
  for (let i = 0; i < myInt; i++) {
    console.log(myStr);
  }
}
