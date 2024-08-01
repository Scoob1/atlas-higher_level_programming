#!/usr/bin/node
const request = require('request');

const film = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/people/';
const characterId = '18/';

request(film, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).result;
    let count =  0;

    films.forEach(function (film) {
      if (film.characters.includes(url + characterId)) {
        count++;
      }
    });
    console.log(count);
}});
