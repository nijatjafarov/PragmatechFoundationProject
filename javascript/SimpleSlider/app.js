var sliderMain = document.querySelector(".slider-main");
var slideCont = document.querySelector(".slide-container");
var slides = document.querySelectorAll(".slide");
var buttons = document.querySelector('.buttons');
var leftBtn = document.getElementById('left');
var rightBtn = document.getElementById('right');
var roundedBtns = document.getElementsByClassName("rounded-button");
var pos = 0;
var slideWidth = sliderMain.offsetWidth;


//sliderMain.style.height = sliderMain.clientWidth*0.7 + 'px';  ISLET




for (var i = 0; i < slides.length; i++) {
  slides[i].style.width = slideWidth + 'px';
}

slideCont.style.width = slideWidth*slides.length + 'px';

roundedBtns[0].style.backgroundColor = "rgba(0, 0, 0, 1)";

var autoScroll = setInterval(scrollRight, 2500);

function currentSlide(position) {
  slideCont.style.transform = `translateX(${position}px)`;

  if (position == 0) {
    leftBtn.style.cursor = "not-allowed";
    leftBtn.disabled = true;
  } else if (position == -(slides.length-1)*slideWidth) {
    rightBtn.style.cursor = "not-allowed";
    rightBtn.disabled = true;
  } else {
    leftBtn.style.cursor = "pointer";
    rightBtn.style.cursor = "pointer";
    rightBtn.disabled = false;
    leftBtn.disabled = false;
  }


}

function buttonShow() {
  buttons.style.width = '60%';
  leftBtn.style.color = "rgba(0, 0, 0, 0.5)";
  rightBtn.style.color = "rgba(0, 0, 0, 0.5)";
}

function buttonHide() {
  buttons.style.width = '70%';
  leftBtn.style.color = "rgba(0, 0, 0, 0)";
  rightBtn.style.color = "rgba(0, 0, 0, 0)";
}

function turnLeft() {
  clearInterval(autoScroll)
  if ( pos <= -slideWidth ) {
    pos += slideWidth;
    currentSlide(pos);
    roundedBtns[Math.abs(pos/slideWidth)].style.backgroundColor = "rgba(0, 0, 0, 1)";
    roundedBtns[Math.abs(pos/slideWidth)].nextElementSibling.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  }
}

function scrollRight() {
  if ( pos >= -slideWidth*(slides.length-2) ) {
    pos -= slideWidth;
    currentSlide(pos);
    roundedBtns[Math.abs(pos/slideWidth)].style.backgroundColor = "rgba(0, 0, 0, 1)";
    roundedBtns[Math.abs(pos/slideWidth)].previousElementSibling.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  }
}

function turnRight() {
  clearInterval(autoScroll);
  scrollRight();
}

function changeSlide(n) {
  clearInterval(autoScroll);
  pos = -slideWidth*n;
  currentSlide(pos);
  for(var i = 0; i < roundedBtns.length; i++) {
    roundedBtns[i].style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  }
  roundedBtns[Math.abs(pos/slideWidth)].style.backgroundColor = "rgba(0, 0, 0, 1)";
}

function hoverColor(button) {
  if (button.style.backgroundColor == "rgba(0, 0, 0, 0.4)") {
    button.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
  }
}

function normalColor(button) {
  if (button.style.backgroundColor == "rgba(0, 0, 0, 0.7)") {
    button.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  }
}

function hoverColorArrow(arrowBtn) {
  arrowBtn.children[0].style.color = "rgba(0, 0, 0, 1)";
}

function normalColorArrow(arrowBtn) {
  arrowBtn.children[0].style.color = "inherit";
}
