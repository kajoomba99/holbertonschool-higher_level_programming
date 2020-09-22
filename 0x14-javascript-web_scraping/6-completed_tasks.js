#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, (err, resp, body) => {
  if (err) return console.log(err);
  const succesTasks = {};
  const jsonResp = JSON.parse(body);
  for (let i = 0; i < jsonResp.length; i++) {
    const task = jsonResp[i];
    if (task.completed === true) {
      const userId = task.userId;
      if (succesTasks[userId]) {
        succesTasks[userId] += 1;
      } else {
        succesTasks[userId] = 1;
      }
    }
  }
  console.log(succesTasks);
});
