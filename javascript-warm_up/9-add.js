#!/usr/bin/node

// Function to add two integers
function add(a, b) {
  return a + b;
}

// Get the command line arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert arguments to integers
const num1 = parseInt(arg1, 10);
const num2 = parseInt(arg2, 10);

// Check if both arguments are provided and valid
if (isNaN(num1) || isNaN(num2)) {
  console.log(NaN);
} else {
  // Call the add function and print the result
  console.log(add(num1, num2));
}
