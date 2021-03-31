var slideWidth = document.querySelector(".slider-main").offsetWidth;
var slideCont = document.querySelector(".slide-container");
var slides = document.querySelectorAll(".slide");
var buttons = document.querySelector('.buttons')
var leftBtn = document.getElementById('left');
var rightBtn = document.getElementById('right');
var roundedBtns = document.getElementsByClassName("rounded-button");
var pos = 0;

for (var i = 0; i < slides.length; i++) {
  slides[i].style.width = slideWidth + 'px';
}

slideCont.style.width = slideWidth*slides.length + 'px';

roundedBtns[0].style.backgroundColor = "rgb(0, 0, 0, 1)";

function autoScroll(){
  hey = setInterval(turnRight, 3000);
}

function currentSlide(position) {
  slideCont.style.transform = `translateX(${position}px)`;
  for(var i = 0; i < roundedBtns.length; i++){
    roundedBtns[i].style.backgroundColor = "rgb(0, 0, 0, 0.4)";
  }
  roundedBtns[Math.abs(position/slideWidth)].style.backgroundColor = "rgb(0, 0, 0, 1)";
}

function buttonShow() {
  buttons.style.width = '60%';
  leftBtn.style.color = "rgb(0, 0, 0, 1)";
  rightBtn.style.color = "rgb(0, 0, 0, 1)";
}

function buttonHide() {
  buttons.style.width = '70%';
  leftBtn.style.color = "rgb(0, 0, 0, 0)";
  rightBtn.style.color = "rgb(0, 0, 0, 0)";
}

function turnLeft() {
  if ( pos <= -slideWidth ) {
    pos += slideWidth;
    currentSlide(pos);
  }
}

function turnRight() {
  if ( pos >= -slideWidth*2 ) {
    pos -= slideWidth;
    currentSlide(pos);
  }
}

function changeSlide(n) {
  pos = -slideWidth*n;
    currentSlide(pos);
}

