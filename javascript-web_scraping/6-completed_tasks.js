#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (completed[todo.userId]) {
          completed[todo.userId]++;
        } else {
          completed[todo.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
