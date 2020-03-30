// Team Muffin Xpress: Brian Moses and Matthew Chan
// SoftDev1 pd2
// K12 -- Ask Circles [Change || Die]
// 2020-03-30

var pic = document.getElementById("vimage");

var drawCircle = function(e){
    var x = e.offsetX;
    var y = e.offsetY;

    var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", "20");
    circle.setAttribute("fill", "blue");
    
    circle.addEventListener("click", circle_clicked);
    
    pic.appendChild(circle);
};

pic.addEventListener("click", drawCircle);

var circle_clicked = function(e){
    e.stopPropagation();
    // console.log(e.originalTarget.getAttribute("fill"));
    if (e.originalTarget.getAttribute("fill") == "blue") {
        e.originalTarget.setAttribute("fill", "cyan");
    }
    else {
        e.originalTarget.setAttribute("cx", Math.random() * pic.getAttribute("width"));
        e.originalTarget.setAttribute("cy", Math.random() * pic.getAttribute("height"));
        e.originalTarget.setAttribute("fill", "blue");
    };
};



var clear = function(e){
    while (pic.lastChild) {
        pic.removeChild(pic.lastChild);
    };
};

var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);