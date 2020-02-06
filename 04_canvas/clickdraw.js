var isRect = true;
var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var newFunction = function(e){
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
	
	var x = event.clientX - 30;   
	var y = event.clientY - 30;
	if (isRect){
		ctx.fillStyle = "#0000FF";
		ctx.fillRect(x,y,100,200);
	}
	else {
		ctx.fillStyle = "#FF0000";
		ctx.beginPath();
		ctx.arc(x, y, 100, 0, 6.28);
		ctx.stroke(); 
		ctx.fill();
	}
	 

};

var clear = function(e){
	ctx.clearRect(0, 0, c.width, c.height);
	console.log(e);


};

var mode = document.getElementById("mode");
mode.addEventListener("click", newFunction);
c.addEventListener("click", draw);

var clearBtn = document.getElementById("clear");
clearBtn.addEventListener("click", clear)

console.log("weqeqwwe");

