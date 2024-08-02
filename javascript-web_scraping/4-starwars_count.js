#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0

  films.forEach(function (film) {
    if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}`)) {
      count++;
    }
  });
    console.log(count);
});
