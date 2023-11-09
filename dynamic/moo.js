let x = 0;
document.getElementById("moobutton").onclick = function (ev) {
    x++;
    ev.target.innerHTML = `Moo! (times ${x})`;
}