#!/usr/bin/node
// Get the arguments
const myVar1 = process.argv[2];
const myVar2 = process.argv[3];

// Convert to integer if possible
const myInt1 = parseInt(myVar1);
const myInt2 = parseInt(myVar2);

// Printing outputs
if (!isNaN(myInt1) && !isNaN(myInt2)) {
  console.log(myInt1 + myInt2);
} else {
  console.log('NaN');
}
