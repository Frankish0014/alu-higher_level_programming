#!/usr/bin/node

// We first get the arguments array from process.argv
const args = process.argv;

// We now extract teh first argument.
const num1 = args[2];

// then convert the first argument to an integer.
const num = parseInt(num1, 10);

// chicking if the conversion is valid or not.
if (num1 === underdefined || isNaN(num)){
	console.log("Not a number";);
} else {
	console.log("My number: " + num);
}
