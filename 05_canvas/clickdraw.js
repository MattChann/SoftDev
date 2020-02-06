// Team M&M: Mo Abedin, Matthew Chan
// SoftDev1 pd2
// K05 -- ...and I want to Paint It Better
// 2020-02-06


var isRect = true;
var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var changeMode = function(e){
    isRect = !isRect;
    var text = document.getElementById("viewMode");
    if (isRect){
        viewMode.innerHTML = "Rectangle";
    }
    else{
        viewMode.innerHTML = "Circle";
    }
};


var draw = function(e){
    var x = e.offsetX;  // gives the exact X coordinate of where the shape is drawn
    var y = e.offsetY;  // gives the exact Y coordinate of where the shape is drawn

    if (isRect){
        ctx.fillStyle = "#0000FF";
        ctx.fillRect(x, y, 70, 70);
    }
    else {
        ctx.fillStyle = "#FF0000";
        ctx.beginPath();    // starts to draw the circle/dot (like netlogo 'pd' or 'pen down')
        ctx.arc(x, y, 10, 0, 6.28);
        ctx.fill();
    }
};


var clear = function(e){
    ctx.clearRect(0, 0, c.width, c.height);
    console.log(e);
};


var mode = document.getElementById("mode");
mode.addEventListener("click", changeMode);
c.addEventListener("click", draw);

var clearBtn = document.getElementById("clear");
clearBtn.addEventListener("click", clear);