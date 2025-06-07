#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from command line arguments
const url = `https://swapi.dev/api/films/${movieId}/`; // Construct the API URL

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters; // Get the list of character URLs

  // Loop through each character URL and fetch character names
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name); // Print the character name
    });
