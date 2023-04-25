#!/usr/bin/node
// Store the 3rd argument
const arg = process.argv[2];
// Convert it to integer
const num = parseInt(arg);
if (Number.isInteger(num)) {
  for (let count = 0; count < num; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
