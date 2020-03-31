var tl = gsap.timeline();

tl.from(".box", {duration: 1, x: "-100", y: 300, scale: 0.5});
tl.to(".box", {duration: 1, x: 300});
tl.to(".box", {duration: 1, y: 500, opacity: "50%", scale: 3});