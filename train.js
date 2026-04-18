console.log("====== MIT TASK with node.js ========")
/*
✨B-TASK (NodeJS)

Shunday function tuzing, u 1ta string parametrga ega bolsin,
hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/
// ✨ MASALANI YECHIMI:
function countDigits(text) {
    let counted = 0;

    for (let i = 0; i < text.length; i++) {
        if (text[i] === "0" ||
            text[i] === "1" ||
            text[i] === "2" ||
            text[i] === "3" ||
            text[i] === "4" ||
            text[i] === "5" ||
            text[i] === "6" ||
            text[i] === "7" ||
            text[i] === "8" ||
            text[i] === "9") {

            counted = counted + 1;
        }
    }

    return counted;
}

const result = countDigits("dhajgsd374bs28eb989bs72hdb1");
console.log(`Bu textda ${result} ta raqam qatnashgan`)



// /* ✨A-TASK:
// Shunday 2 parametrli function tuzing, 
// hamda birinchi parametrdagi letterni ikkinchi parametrdagi 
// so'zdan qatnashga sonini return qilishi kerak boladi.
// MASALAN countLetter("e", "engineer") 3ni return qiladi.
// */

// // ✨ MASALANI YECHIMI:
// let letters = 0;
// let countedLetter = 0;

// function count(letter, word) {
//     while (letters < word.length) {
//         if (word[letters] === letter) {
//             countedLetter = countedLetter + 1
//         }
//         letters = letters + 1
//     }
//     return countedLetter;

// };
// let letter = "s";
// let word = "success_stories";
// let result = count(letter, word);
// console.log(`${letter} is used ${result} times in ${word} word`);
