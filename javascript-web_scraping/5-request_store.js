#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url)
  .pipe(fs.createWriteStream(filePath))
  .on('finish', () => {
    console.log(`Downloaded and saved ${fs.statSync(filePath).size} bytes to ${filePath}`);
  });

