//=============================== MIT TASK with node.js ==============================================
/*
//                                  ✨E-TASK (NodeJS)
//=====================================================================================================
// E-TASK (NodeJS)

// Shunday function tuzing, u bitta string argumentni qabul qilib
// o'sha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"
//===================================================================================================== */
// ✨ MASALANI YECHIMI:

function getReverse(txt) {
    let reverseLetter = txt.split("").reverse().join("");
    return reverseLetter;
}

let result = getReverse("oq balkim qora bo'lib qora oq bo'lib chiqsachi");
console.log("result :", result,);










//                                  ✨D-TASK (NodeJS)
//=====================================================================================================
// D-TASK (NodeJS)

// Shunday function tuzingki unga integerlardan iborat array pass bolsin va
// function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
//=====================================================================================================
// ✨ MASALANI YECHIMI:

// function getHighestIndex(arr) {
//     let index = 0;
//     for (let i = 1; i < arr.length; i++) {
//         if (arr[i] > arr[index]) {
//             index = i
//         }

//     }
//     return index;
// }

// const result = getHighestIndex([-5, 31, 43, 25, 4]);
// console.log("result:", result)


// /*
//                                  ✨C-TASK (NodeJS)
//=====================================================================================================
// Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string
// bir hil harflardan iborat bolsa true aks holda false qaytarsin MASALAN :
// checkContent("mitgroup", "gmtiprou") return qiladi true;
//=====================================================================================================
// ✨ MASALANI YECHIMI:

// function checkContent(matn1, matn2) {

//     if (matn1.length !== matn2.length) {
//         return false;
//     }

//     let result = true;

//     for (let harf = 0; harf < matn1.length; harf++) {
//         result = result && matn2.includes(matn1[harf]);
//     }

//     return result;
// }

// let result = checkContent("realmadrid", "dirdmalaer");
// console.log("result:", result);






// ✨B-TASK (NodeJS)

// Shunday function tuzing, u 1ta string parametrga ega bolsin,
// hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
// MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
// */
// // ✨ MASALANI YECHIMI:
// function countDigits(text) {
//     let counted = 0;

//     for (let i = 0; i < text.length; i++) {
//         if (text[i] === "0" ||
//             text[i] === "1" ||
//             text[i] === "2" ||
//             text[i] === "3" ||
//             text[i] === "4" ||
//             text[i] === "5" ||
//             text[i] === "6" ||
//             text[i] === "7" ||
//             text[i] === "8" ||
//             text[i] === "a" ||
//             text[i] === "9") {

//             counted = counted + 1;
//         }
//     }

//     return counted;
// }

// const result = countDigits("37dhajgsd4bs28eb989bs72hdb1");
// console.log(`Bu textda ${result} ta raqam qatnashgan`)



// // /* ✨A-TASK:
// // Shunday 2 parametrli function tuzing, 
// // hamda birinchi parametrdagi letterni ikkinchi parametrdagi 
// // so'zdan qatnashga sonini return qilishi kerak boladi.
// // MASALAN countLetter("e", "engineer") 3ni return qiladi.
// // */

// // // ✨ MASALANI YECHIMI:
// // let letters = 0;
// // let countedLetter = 0;

// // function count(letter, word) {
// //     while (letters < word.length) {
// //         if (word[letters] === letter) {
// //             countedLetter = countedLetter + 1
// //         }
// //         letters = letters + 1
// //     }
// //     return countedLetter;

// // };
// // let letter = "s";
// // let word = "success_stories";
// // let result = count(letter, word);
// // console.log(`${letter} is used ${result} times in ${word} word`);


// function countNumbers(str) {
//     let count = 0;

//     for (let char of str) {
//         if (char <= '9') {
//             count++;
//         }
//     }

//     return count;
// }

// let result = countNumbers("ajd2-129efdqfq");
// console.log("result:", result);