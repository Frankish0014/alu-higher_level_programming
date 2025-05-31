#!/usr/bin/node

// Get the first argument from the command line
const x = process.argv[2];

// Check if the argument is a valid positive integer
const num = parseInt(x, 10);

// If num is NaN or less than 1, print the error message
if (isNaN(num) || num < 1) {
  console.log("Missing number of occurrences");
} else {
// Loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log("C is fun");
  }
}
