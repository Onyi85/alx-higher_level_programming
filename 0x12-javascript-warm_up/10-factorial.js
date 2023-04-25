#!/usr/bin/node
// setting the first argument
const arg = process.argv[2];
// convert it to int
const num = parseInt(arg);
// Writing the factorial function
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const result = factorial(num);
console.log(result);
