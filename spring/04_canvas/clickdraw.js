// Team M&M: Mo Abedin, Matthew Chan
// SoftDev1 pd2
// K04 -- I See a Red Door...
// 2020-02-05


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
    var x = e.clientX;
    var y = e.clientY;

    if (isRect){
        ctx.fillStyle = "#0000FF";
        ctx.fillRect(x, y, 70, 70);
    }
    else {
        ctx.fillStyle = "#FF0000";
        ctx.beginPath();
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