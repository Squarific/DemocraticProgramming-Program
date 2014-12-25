// Menu script
// Cool stuff
var quit = false;
var commandos = {
    quit: function () {
        return true;
    }
}

while (!quit) {
    var inputString = prompt("What do you want to do?");
    var inputArray = inputString.split(" ");

    if (typeof commandos[inputArray[0]] === "function") {
        quit = commandos[inputArray[0]].apply(commandos, inputArray);
    }
}
