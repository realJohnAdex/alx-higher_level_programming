#!/usr/bin/node
// Getting the lenght of the args
const argLen = process.argv.length - 2;

// Print outpust
if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
