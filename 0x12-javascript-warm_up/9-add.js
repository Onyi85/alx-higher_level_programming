#!/usr/bin/node
// copy the array
const args = process.argv.slice(2);
function add (a = args[0], b = args[1]) {
  console.log(Number(a) + Number(b));
}
// invoking the function
add(args[0], args[1]);
