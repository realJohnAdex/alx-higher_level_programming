#!/usr/bin/node
// Create an array of strings
const myStr = 'X';
const myArg = process.argv[2];

const myInt = parseInt(myArg);
// Use console.log(...) to print the value of myVar
if (!isNaN(myInt)) {
  for (let j = 0; j < myInt; j++) {
    let line = '';

    for (let i = 0; i < myInt; i++) {
      line += myStr;
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
