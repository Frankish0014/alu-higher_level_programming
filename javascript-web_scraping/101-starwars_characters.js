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
    const film = JSON.parse(body);
    const characters = film.characters;

    const fetchCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, characterBody) => {
          if (error) {
            reject(error);
          } else {
            try {
              const name = JSON.parse(characterBody).name;
              resolve(name);
            } catch (parseErr) {
              reject(parseErr);
            }
          }
        });
      });
    };

    (async () => {
      for (const url of characters) {
        try {
          const name = await fetchCharacterName(url);
          console.log(name);
        } catch (error) {
          console.error(error);
        }
      }
    })();
  } catch (parseError) {
    console.error('Invalid JSON:', parseError.message);
  }
});
