// Team Silly Goobers: David Lupea and Matthew Chan
// SoftDev1 pd2
// K14 -- Ask Circles [Change || Die] While Moving, etc.
// 2020-03-31

var button = document.getElementById('clear');
var pic = document.getElementById('vimage');
var btn_move = document.getElementById('move');
var btn_xtra = document.getElementById('xtra');

var plot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    if(e.target.getAttribute("id") == "vimage"){
        c.setAttribute("cx", e.offsetX);
        c.setAttribute("cy", e.offsetY);
        c.setAttribute("r", 20);
        c.setAttribute("dx", 1);
        c.setAttribute("dy", 1);
        c.setAttribute("fill", "blue");
        pic.appendChild(c);
    }
}

var isAnimating = false;
var animation_id;

var stop = function(e) {
    if (isAnimating) {
        isAnimating = false;
        window.cancelAnimationFrame(animation_id);
    }
}

var move = function(e) {
    stop();    
    isAnimating = true;

    for(var i = 0; i < pic.children.length; i++){
        x =  parseInt(pic.children[i].getAttribute("cx"));
        y =  parseInt(pic.children[i].getAttribute("cy"));
        dx = parseInt(pic.children[i].getAttribute("dx"));
        dy = parseInt(pic.children[i].getAttribute("dy"));

        pic.children[i].setAttribute("cx", x + dx);
        pic.children[i].setAttribute("cy", y + dy);

        if (x < 20 || x > pic.getAttribute("width") - 20) {
            pic.children[i].setAttribute("dx", -dx);
            pic.children[i].setAttribute("cx", x - dx);
        }
        if (y < 20 || y > pic.getAttribute("height") - 20) {
            pic.children[i].setAttribute("dy", -dy);
            pic.children[i].setAttribute("cy", y - dy);
        }
    }
    animation_id = window.requestAnimationFrame(move);
}

var xtra = function(e) {
    stop();
    isAnimating = true;
    
    for(var i = 0; i < pic.children.length; i++){
        x =  parseInt(pic.children[i].getAttribute("cx"));
        y =  parseInt(pic.children[i].getAttribute("cy"));
        dx = parseInt(pic.children[i].getAttribute("dx"));
        dy = parseInt(pic.children[i].getAttribute("dy"));

        pic.children[i].setAttribute("cx", x + dx);
        pic.children[i].setAttribute("cy", y + dy);
        
        if (x < 20 || x > pic.getAttribute("width") - 20) {
            pic.children[i].setAttribute("dx", -dx);
            pic.children[i].setAttribute("cx", x - dx);
        }
        if (y < 20 || y > pic.getAttribute("height") - 20) {
            pic.children[i].setAttribute("dy", -dy);
            pic.children[i].setAttribute("cy", y - dy);
        }
        
        for(var j = 0; j < pic.children.length; j++){
            other_x = parseInt(pic.children[j].getAttribute("cx"));
            other_y = parseInt(pic.children[j].getAttribute("cy"));
            if (Math.sqrt(Math.pow(x-other_x, 2) + Math.pow(y - other_y, 2)) != 0 && Math.sqrt(Math.pow(x - other_x, 2)+Math.pow(y - other_y, 2)) < 40 && Math.abs(y - other_y) != 1 && Math.abs(x - other_x) != 1){
                max = Math.max(i, j)
                min = Math.min(i, j)
                pic.children[max].remove()
                pic.children[min].remove()
            }
        }
    }
    animation_id = window.requestAnimationFrame(xtra);
}

var clear = function(e) {
    stop();
    while (pic.lastChild) {
        pic.removeChild(pic.lastChild);
    }
};

button.addEventListener('click', clear);
pic.addEventListener('click', plot);
btn_move.addEventListener('click', move);
btn_xtra.addEventListener('click', xtra);
