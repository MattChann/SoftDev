// Team No Makeup: Matthew Chan, Derek Leung
// SoftDev1 pd2
// K07 -- They lock us in the tower whenever we get caught
// 2020-02-12


var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var isAnimating = false;
var animationId;

var animate = function(e){
    // if (!isAnimating){
    ctx.beginPath();    // starts to draw the circle/dot (like netlogo 'pd' or 'pen down')
    ctx.arc(100, 100, 10, 0, 6.28);
    ctx.fillStyle = "#D8E4FF";
    ctx.fill();

        // animationId = window.requestAnimationFrame(animate);
    // }
};

var animateButton = document.getElementById("animate");
animateButton.addEventListener("click", animate);



// var stop = function(e){
//     if (isAnimating){
//         window.cancelAnimationFrame(animationId);
//     }
// };

// var stopButton = document.getElementById("stop");
// stopButton.addEventListener("click", stop);