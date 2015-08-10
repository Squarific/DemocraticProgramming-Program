console.log("You are playing hangman! Press letters that you think are in the word.");
var words = ["test", "tree", "programming"];
var word = words[Math.floor(Math.random() * words.length)];
var guessedLetters = [];
document.addEventListener("keydown", function (event) {
    var letter = event.key || String.fromCharCode(event.which || event.keyCode)
    console.log("You guessed the letter " + letter);
});