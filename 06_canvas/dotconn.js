// Matthew Chan
// SoftDev1 pd2
// K06 -- Dot Dot Dot
// 2020-02-11


var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var clear = function(e){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    isFirstDot = true;
};

var clearBtn = document.getElementById("clear");
clearBtn.addEventListener("click", clear);



var isFirstDot = true;
var previousPointX;
var previousPointY;

var draw = function(e){
    var x = e.offsetX;  // gives the exact X coordinate of where the shape is drawn
    var y = e.offsetY;  // gives the exact Y coordinate of where the shape is drawn

    ctx.beginPath();    // starts to draw the circle/dot (like netlogo 'pd' or 'pen down')
    ctx.arc(x, y, 10, 0, 6.28);
    ctx.fillStyle = "#D8E4FF";
    ctx.fill();

    if (isFirstDot) {
        isFirstDot = false;
    }
    else {
        ctx.beginPath();
        ctx.moveTo(previousPointX, previousPointY);
        ctx.lineTo(x, y);
        ctx.strokeStyle = "#B3679B";
        ctx.stroke();
    }

    previousPointX = x;
    previousPointY = y;
};

canvas.addEventListener("click", draw);