var pic = document.getElementById("vimage");

var isFirstDot = true;
var previousX;
var previousY;

var drawDot = function(e){
    var x = e.offsetX;
    var y = e.offsetY;

    var dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    dot.setAttribute("cx", x);
    dot.setAttribute("cy", y);
    dot.setAttribute("r", "10");
    dot.setAttribute("fill", "#D8E4FF");

    pic.appendChild(dot);

    if (isFirstDot) {
        isFirstDot = false;
    }
    else {
        var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", previousX);
        line.setAttribute("y1", previousY);
        line.setAttribute("x2", x);
        line.setAttribute("y2", y);
        line.setAttribute("stroke", "#B3679B");

        pic.appendChild(line);
    }

    previousX = x;
    previousY = y;
};

pic.addEventListener("click", drawDot);



var clear = function(e){
    pic.innerHTML = "";
    isFirstDot = true;
};

var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);