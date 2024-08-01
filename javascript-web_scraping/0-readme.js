#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];

fs.readFile(fp, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
