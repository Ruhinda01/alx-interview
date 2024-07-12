#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('movieId is required');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, async (error, response, body) => {
  if (error) console.log(error);
  const charactersURL = JSON.parse(body).characters;

  for (const character of charactersURL) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) console.log(error);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
