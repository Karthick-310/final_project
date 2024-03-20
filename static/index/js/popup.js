
var popup_biology = document.getElementById('popup-biology');
var btn_biology = document.getElementById("popup-btn-biology");
var span_biology = document.getElementById("close-biology");
btn_biology.onclick = function() {
    popup_biology.classList.add('show');
}
span_biology.onclick = function() {
    popup_biology.classList.remove('show');
}

window.onclick = function(event) {
    if (event.target == popup_biology) {
        popup_biology.classList.remove('show');
    }
}

// science 
var popup_science = document.getElementById('popup-science');
var btn_science = document.getElementById("popup-btn-science");
var span_science = document.getElementById("close-science");
btn_science.onclick = function() {
    popup_science.classList.add('show');
}
span_science.onclick = function() {
    popup_science.classList.remove('show');
}

window.onclick = function(event) {
    if (event.target == popup_science) {
        popup_science.classList.remove('show');
    }
}

// Arts
var popup_arts = document.getElementById('popup-arts');
var btn_arts = document.getElementById("popup-btn-arts");
var span_arts = document.getElementById("close-arts");
btn_arts.onclick = function() {
    popup_arts.classList.add('show');
}
span_arts.onclick = function() {
    popup_arts.classList.remove('show');
}

window.onclick = function(event) {
    if (event.target == popup_arts) {
        popup_arts.classList.remove('show');
    }
}
// commerce
var popup_commerce = document.getElementById('popup-commerce');
var btn_commerce = document.getElementById("popup-btn-commerce");
var span_commerce = document.getElementById("close-commerce");
btn_commerce.onclick = function() {
    popup_commerce.classList.add('show');
}
span_commerce.onclick = function() {
    popup_commerce.classList.remove('show');
}

window.onclick = function(event) {
    if (event.target == popup_commerce) {
        popup_commerce.classList.remove('show');
    }
}