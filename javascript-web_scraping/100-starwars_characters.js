#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  try {
    const characters = JSON.parse(body).characters;

    const fetchCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, characterBody) => {
          if (error) {
            reject(error);
          } else {
            const name = JSON.parse(characterBody).name;
            resolve(name);
          }
        });
      });
    };

    // Sequential output to maintain order
    (async () => {
      for (const url of characters) {
        try {
          const name = await fetchCharacter(url);
          console.log(name);
        } catch (fetchError) {
          console.error(fetchError);
        }
      }
    })();
  } catch (parseError) {
    console.error('Invalid JSON response:', parseError.message);
  }
});
