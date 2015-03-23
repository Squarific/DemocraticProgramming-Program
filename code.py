
var commandos = { "1" : { "apply" : function(c, i) { return true; }}};

 
 
    var inputArray = inputString.split(" ");
        quit = commandos[inputArray[0]].apply(commandos, inputArray);
}
