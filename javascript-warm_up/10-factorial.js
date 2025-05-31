#!/usr/bin/node

// Recursive function to compute factorial
function factorial(n) {
  // Base case: factorial of 0 or 1 is 1
  if (n <= 1) {
    return 1;
  }

  // Recursive case
  return n * factorial(n - 1);
}

// Get the command line argument
const arg = process.argv[2];

// Convert argument to an integer
const num = parseInt(arg, 10);

// Check if num is NaN
if (isNaN(num)) {
  console.log(1); // Factorial of NaN is defined as 1
} else {
  // Compute and print the factorial
  console.log(factorial(num));
}

