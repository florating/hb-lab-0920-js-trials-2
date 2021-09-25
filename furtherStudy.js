"use strict";

const words = new Set();

const animals = new Set(['python', 'zebra']);

function wordsInCommon(words1, words2) {
    const words1Set = new Set(words1);
    const words2Set = new Set(words2);
    const result = new Set();
    for (const word of words1Set) {
        if (words2Set.has(word)) {
            result.add(word);
        }
    }
    return Array.from(result);
}


function kidsGame(names) {
    const output = [names.shift()]; // removes an item from the beginning of the Array
    const lettersToWords = {};

    for (const n of names) {
        if (lettersToWords[n[0]] === undefined) {
            lettersToWords[n[0]] = [n];
        } else {
            lettersToWords[n[0]].push(n);
        }
    }

    while (true) {
        const lastWord = output[output.length - 1];
        // console.log(`lastWord is ${lastWord}, output.length is ${output.length}`);
        const lastLetter = lastWord[lastWord.length - 1];
        // console.log(`lastLetter is ${lastLetter}`);
        // console.log(`lettersToWords['${lastLetter}'] = ${lettersToWords[lastLetter]}`);
        if (
          lettersToWords[lastLetter] === undefined ||
          lettersToWords[lastLetter].length === 0
        ) {
            break;
        }
        let word = lettersToWords[lastLetter].shift();
        output.push(word);
        // console.log(`Just added word = ${word} to output = ${output}.`);
    }
    return output;
}

console.log(kidsGame(["noon", "naan", "nun"]));
console.log(kidsGame(["apple", "berry", "cherry"]));
