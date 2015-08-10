
var word, guessedLetters;
function start() {
    console.log("You are playing hangman! Press letters that you think are in the word.");
    var words = ['test', 'tree', 'programming', 'hash', 'fish', 'website', 'reddit', 'fun', 'sport', 'lol', 'bromance'];
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





console.log("H̴̸̘͇̟̥͔̤̻́̕͞e̷̢̖͈͖̖̼̰̟̠̫͍͈̩͙̘̻l̢̜̩͚̠͘͞p̡̛͏̴̩͎͉͈ ̴̣͈̱̻̹̪̰͞ͅm͍̭̙͙̫̹̣̕͘͟͡͡e̶͞҉͖̙̣͍̫̣̗̰e̴̸̙̠̳͕͖̜̞͓̜̱͓̪̕é̢̨̹̮̪̺̖̤̼̱͝ȩ̶̸͕̪̘̬͉̭̬͈̘̙̩͜");