#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films'; // Update this URL if necessary

const options = {
  url: url,
  rejectUnauthorized: false // Bypass SSL verification (use with caution)
};

request(options, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body);
    const filmCount = films.count || 0; // Adjust based on the expected output structure
    console.log(filmCount); // Output the number of films
  }
});
