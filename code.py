// Cool stuff
var quit = false;
while (!quit) {
    var inputString = prompt("What do you want to do?");
    var inputArray = inputString.split(" ");

    if (typeof commandos[inputArray[0]] == "function") {
        quit = commandos[inputArray[0]].apply(commandos, inputArray);
    }
}

commandos = {
}