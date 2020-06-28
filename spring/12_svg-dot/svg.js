var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");
var l, c;

var lastX = -1;
var lastY;

var clear = function() {
  pic.innerHTML = '';
  lastX = -1;
}

var plot = function(e) {
  if (lastX == -1) {
    lastX = e.offsetX;
    lastY = e.offsetY;
  }

  l = document.createElementNS(
  "http://www.w3.org/2000/svg", "line");

  l.setAttribute("x1", lastX);
  l.setAttribute("y1", lastY);
  l.setAttribute("x2", e.offsetX);
  l.setAttribute("y2", e.offsetY);
  l.setAttribute("stroke", "black");


  c = document.createElementNS(
  "http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", e.offsetX);
  c.setAttribute("cy", e.offsetY);
  c.setAttribute("r", 20);
  c.setAttribute("fill", "black");

  lastX = e.offsetX;
  lastY = e.offsetY;

  pic.appendChild(l);
  pic.appendChild(c);
}

pic.addEventListener("click", plot);
btn.addEventListener("click", clear);
