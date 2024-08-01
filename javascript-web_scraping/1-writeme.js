#!/usr/bin/node
const fs = require('fs');

const fp = process.argv[2];
const string = process.argv[3];

fs.writeFile(fp, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
