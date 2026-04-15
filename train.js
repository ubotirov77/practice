console.log("====== MIT TASK A with node.js ========")
// MIT Task A
let letters = 0;
let countedLetter = 0;

function count(letter, word) {
    while (letters < word.length) {
        if (word[letters] === letter) {
            countedLetter = countedLetter + 1
        }
        letters = letters + 1
    }
    return countedLetter;

};
let letter = "s";
let word = "success_stories";
let result = count(letter, word);
console.log(`${letter} is used ${result} times in ${word} word`);