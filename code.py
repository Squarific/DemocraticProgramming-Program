console.log("You are playing hangman! Press letters that you think are in the word.");
var words = ["test", "tree", "programming"];
var word = words[Math.floor(Math.random() * words.length)];
var guessedLetters = [];
document.addEventListener("keydown", function (event) {
var letter = event.key || String.fromCharCode(event.which || event.keyCode);
    console.log("You guessed the letter " + letter);
    if (guessedLetters.indexOf(letter) !== -1) {
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