#!/usr/bin/node

// Collecting the first argument
const sqsize = process.argv[2];

const nums = parseInt(sqsize, 10);

if (isNaN(nums) || nums < 1){
	console.log('Missing size');
} else {
	for (let i = 0; i < nums; i++){
		let row='';
		for (let j = 0; j < nums; j++){
			row += 'X';
		}
		console.log(row);
	}
}
