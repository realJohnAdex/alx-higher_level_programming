#!/usr/bin/node
// Function to compute factorial recursively
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

// Get the arguments
const myInt = parseInt(process.argv[2]);

// Printing outputs
console.log(factorial(myInt));
