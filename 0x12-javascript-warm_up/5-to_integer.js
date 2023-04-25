#!/usr/bin/node
// copy the array
const args = process.argv.slice(2);
// Convert it to integer
const num = parseInt(args);
if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
