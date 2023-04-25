#!/usr/bin/node
// copy the third argument
const arg = process.argv[2];
// convert it to an int
const num = parseInt(arg);
if (Number.isInteger(num)) {
  let letterX = [];
  for (let count = 0; count < num; count++) {
    letterX += 'X';
  }
  for (let count = 0; count < num; count++) {
    console.log(letterX);
  }
} else {
  console.log('Missing size');
}
