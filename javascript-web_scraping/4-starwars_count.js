#!/usr/bin/node

const request = require('request');

const url = 'https://swapi.dev/api/people/18/'; // Wedge Antilles' ID

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const character = JSON.parse(body);
    const filmCount = character.films.length; // Count the number of films

    console.log(filmCount); // Output the number of films
  }
});
