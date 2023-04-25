#!/usr/bin/node
// copy the array
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  // converting the array to Number
  const nums = args.map(Number);
  // sort in ascending order
  nums.sort((a, b) => a - b);
  // print the output
  console.log(nums[nums.length - 2]);
}
