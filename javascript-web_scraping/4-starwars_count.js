#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const results = data.results || [];
    const count = results.filter(film => film.characters.includes(wedgeUrl)).length;
    console.log(count);
  } catch (err) {
    console.error('Error parsing response:', err);
  }
});
