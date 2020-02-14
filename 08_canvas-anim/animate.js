// Team No Makeup: Matthew Chan, Derek Leung
// SoftDev1 pd2
// K08 -- What is it saving the screen from?
// 2020-02-13


var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var isAnimating = false;
var animationId;


var radius = 0;
var adjust = 1;

var circle_animateStart = function(e) {
    stop();     // Allows users to change animations without having to click stop
    window.requestAnimationFrame(circle_animate);
    isAnimating = true;
};

var circle_animate = function(e) {
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
    animationId = window.requestAnimationFrame(circle_animate);
};

var circle_animateButton = document.getElementById("animate-circle");
circle_animateButton.addEventListener("click", circle_animateStart);

//==============================================================================

var dvd_logo = new Image(90, 60);
dvd_logo.src = "https://raw.githubusercontent.com/stuy-softdev/notes-and-code19-20/master/smpl/200214f_js-canvas-anim/logo_dvd.jpg?token=ALKY4H5L3CDWQZ46ZGAS6E26J2JTK";
// dvd_logo.width = 0.15 * Math.min(canvas.width, canvas.height);
// dvd_logo.height = dvd_logo.width * (dvd_logo.naturalHeight / dvd_logo.naturalWidth);

var x;
var y;
var xAdjust;
var yAdjust;

var dvd_animateStart = function(e) {
    stop();     // Allows users to change animations without having to click stop
    window.requestAnimationFrame(dvd_animate);
    isAnimating = true;

    x = Math.round(Math.random() * (canvas.width - dvd_logo.width));
    y = Math.round(Math.random() * (canvas.height - dvd_logo.height));
    xAdjust = 1;
    yAdjust = 1;
};

var dvd_animate = function(e) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);   // Clears the canvas first

    if (x >= (canvas.width - dvd_logo.width)) {
        xAdjust = -1;
    }
    if (y >= (canvas.height - dvd_logo.height)) {
        yAdjust = -1;
    }
    if (x <= 0) {
        xAdjust = 1;
    }
    if (y <= 0) {
        yAdjust = 1;
    }
    x += xAdjust;
    y += yAdjust;

    ctx.drawImage(dvd_logo, x, y, dvd_logo.width, dvd_logo.height);

    animationId = window.requestAnimationFrame(dvd_animate);
};

var dvd_animateButton = document.getElementById("animate-dvd");
dvd_animateButton.addEventListener("click", dvd_animateStart);

//==============================================================================

var stop = function(e) {
    // Checks if already animating so clicking the animate button again won't break things
    if (isAnimating) {
        isAnimating = false;
        window.cancelAnimationFrame(animationId);
    }
};

var stopButton = document.getElementById("stop");
stopButton.addEventListener("click", stop);
