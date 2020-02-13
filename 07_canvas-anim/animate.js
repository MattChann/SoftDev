// Team No Makeup: Matthew Chan, Derek Leung
// SoftDev1 pd2
// K07 -- They lock us in the tower whenever we get caught
// 2020-02-12


var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var isAnimating = false;
var animationId;
var radius = 0;
var adjust = 1;

var animateStart = function(e) {
    // Checks if already animating so clicking the animate button again won't break things
    if (!isAnimating) {
        window.requestAnimationFrame(animate);
        isAnimating = true;
    }
};

var animate = function(e) {
    // If the current radius of the drawn circle hits any edge, start shrinking the circle
    if (radius >= Math.round((Math.min(canvas.width, canvas.height)) / 2)) {
        adjust = -1;
    }
    // If the current radius of the drawn circle is 0, start expanding the circle
    if (radius <= 0) {
        adjust = 1;
    }
    // Adjust the intended radius of the next circle to be drawn
    radius+=adjust;

    ctx.clearRect(0, 0, canvas.width, canvas.height);   // Clears the canvas first
    // Draws the new circle centered on the canvas with the new radius
    ctx.beginPath();
    ctx.arc((canvas.width / 2), (canvas.height / 2), radius, 0, 6.28);
    ctx.fillStyle = "#D8E4FF";
    ctx.fill();
    animationId = window.requestAnimationFrame(animate);
};

var animateButton = document.getElementById("animate");
animateButton.addEventListener("click", animateStart);



var stop = function(e) {

    // Checks if already animating so clicking the animate button again won't break things
    if (isAnimating) {
        isAnimating = false;
        window.cancelAnimationFrame(animationId);
    }
};

var stopButton = document.getElementById("stop");
stopButton.addEventListener("click", stop);