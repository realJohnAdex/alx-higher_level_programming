#!/usr/bin/node
// Get the first argument
const myVar = process.argv[2];

// Convert to integer if possible
const myInt = parseInt(myVar);

// Printing outputs
if (!isNaN(myInt)) {
  console.log(`My number: ${myInt}`);
} else {
  console.log('Not a number');
}
