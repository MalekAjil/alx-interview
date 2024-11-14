#!/usr/bin/node
/**
 * Script to print all characters of a Star Wars movie
 */

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch data from the API');
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } else {
          reject(new Error('Failed to fetch character data'));
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
