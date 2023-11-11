let x = 0;
document.getElementById("moobutton").onclick = function (ev) {
    x++;
    ev.target.innerHTML = `Moo! (times ${x})`;
}

window.onload = function (l) {
    // are you a human or at least a javascript-executing robot? hehe:3
    fetch("/human");
}