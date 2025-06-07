#!/usr/bin/node
const { list } = require('./100-data.js');
console.log(list);
const newList = list.map((value, index) => value * index);
console.log(newList);

