#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, res, body) => {
  if (error) {
    console.errror(error);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
