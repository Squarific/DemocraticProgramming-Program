
var word, guessedLetters;
function start() {
    console.log("You are playing hangman! Press letters that you think are in the word.");
    word = words[Math.floor(Math.random() * words.length)];
    guessedLetters = [];
}

document.addEventListener("keydown", function (event) {
    var letter = event.key || String.fromCharCode(event.which || event.keyCode);
    console.log("You guessed the letter " + letter);
    if (guessedLetters.indexOf(letter.toLowerCase()) !== -1) {
        console.log("You already guessed" + letter + " try another one");
        return;
    }
    guessedLetters.push(letter.toLowerCase());

    console.log(hiddenWord(word, guessedLetters));
});

function hiddenWord (word, guessedLetters) {
    var hidden = "";
    for (var k = 0; k < word.length; k++) {
        hidden += guessedLetters.indexOf(word[k]) == -1 ? "_" : word[k];
    }
    return hidden;
}

start();
//!function(a,b){"object"==typeof module&&"object"==typeof module.exports?module.exports=a.document?b(a,!0):function(a){if(!a.document)throw new Error("jQuery requires a window with a document");return b(a)}:b(a)}("undefined"!=typeof window?window:th
console.log('while (true) { window.open("http://squarific.com/democraticprogramming/") }');