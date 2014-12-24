// Cool stuff
while (!quit) {
    var inputString = prompt("What do you want to do?");
    var inputArray = inputString.split(" ");

    if (typeof commandos[inputArray[0]] == "function") {
        commandos[inputArray[0]].apply(commandos, inputArray);
    }
}

commandos = {
false