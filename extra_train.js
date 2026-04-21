const animal_list = ["fox", "ant", "bird", "lion", "lion", "wolf", "deer", "frog", "hen",
    "mole", "duck", "goat", "dog", "cat", "bat", "cock", "cow"];

function findAnimal(text) {
    let count = 0
    let findAnimal = []
    for (let animal = 0; animal < animal_list.length; animal++) {

        for (let letter = 0; letter < animal_list[animal].length; letter++) {
            for (let data = 0; data < text.length; data++) {
                if (text.length >= animal_list[animal].length) {
                    if (text[data] === animal_list[animal][letter]) {
                        count++

                        if (count === animal_list[animal].length) { //agotd

                            findAnimal.push(animal_list[animal])
                            count = 0
                        }
                    }
                }
            }
        }
        count = 0
        
    }
    
    return findAnimal;
}
const javob = findAnimal("aglfkobcwtd");
console.log("javob=>", javob);

