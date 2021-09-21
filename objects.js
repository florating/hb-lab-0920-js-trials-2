"use strict";


// 1. countWords
function countWords(phrase) {
  const wordCounts = {};
  for (const word of phrase.split(' ')) {
    if (wordCounts.includes(word)) {
      wordCounts[word] += 1;
    }
    else {
      wordCounts[word] = 1;
    }
  }
  return wordCounts;
}


// 2. getMelonsAtPrice
function getMelonsAtPrice(price) {
  // Replace this with your code
}
