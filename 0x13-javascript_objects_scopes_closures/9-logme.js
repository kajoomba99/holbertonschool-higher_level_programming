#!/usr/bin/node
function logMe (item) {
  if (typeof logMe.counter === 'undefined') {
    logMe.counter = 0;
  }
  console.log(logMe.counter + ': ' + item
  );
  logMe.counter++;
}

exports.logMe = logMe;
