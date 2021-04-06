var header = document.querySelector(".header")
var navbar = document.querySelector(".navbar");
var navbarSections = navbar.getElementsByTagName("li");
var highlighter = document.querySelector(".highlighter");
var scrollHeader = document.querySelector(".scroll");
var scrollSections = scrollHeader.getElementsByTagName("li");
var scrollHighlighter = scrollHeader.querySelector(".highlighter");
var hamburgerMenu = document.querySelector(".hamburger-menu");
var openedMenu = document.querySelector(".opened-menu");
var backToTop = document.querySelector(".back-to-top");
var about = document.querySelector(".about");
var firstScreen = document.querySelector(".first-screen");
var restOfPage = document.querySelector(".rest-of-page");
var smSideBar = document.querySelector(".sm-sidebar")
var open = false;

firstScreen.style.height = window.innerHeight - 105 + "px";

var workSquares = document.querySelectorAll(".work-square");
var squares = document.querySelectorAll(".square");
for( var i = 0; i < squares.length; i++) {
  squares[i].style.height = squares[i].clientWidth + "px";
}
for( var i = 0; i < workSquares.length; i++) {
  workSquares[i].style.height = workSquares[i].clientWidth - 24 + "px";
}

openedMenu.style.width = document.body.offsetWidth-100 + "px";

function dynamicSizes() {
  openedMenu.style.width = document.body.offsetWidth-100 + "px";
  firstScreen.style.height = firstScreen.offsetWidth*0.447 + "px";
  for( var i = 0; i < squares.length; i++) {
    squares[i].style.height = squares[i].clientWidth + "px";
  }
  for( var i = 0; i < workSquares.length; i++) {
    workSquares[i].style.height = workSquares[i].clientWidth - 24 + "px";
  }
}

function highlight(num) {
  highlighter.style.width = navbarSections[num].offsetWidth + "px";
  scrollHighlighter.style.width = scrollSections[num].offsetWidth + "px";
  var navPos = 0;
  var scrollPos = 0;
  for (var i = 0; i < num; i++) {
    navPos += navbarSections[i].offsetWidth;
    scrollPos += scrollSections[i].offsetWidth;
  }
  highlighter.style.left = navPos + "px";
  scrollHighlighter.style.left = scrollPos + "px";
}

function openCloseMenu() {
  if(open) {
    openedMenu.style.height = "0";
    openedMenu.style.border = "none";
    header.style.borderBottom = "1px solid #ebebeb";
    open = false;
  } else {
    openedMenu.style.height = "auto";
    openedMenu.style.borderBottom = "1px solid #ebebeb";
    header.style.border = "none";
    open = true;
  }
}

function hoverMenuItem(listItem) {
  listItem.firstElementChild.style.color = "#cbcbcb";
}

function normalMenuItem(listItem) {
  listItem.firstElementChild.style.color = "black";
}

window.onscroll = function() {scroll()};

function scroll() {
  if (document.documentElement.scrollTop > 114) {
    if (openedMenu.offsetHeight != 0) {
      scrollHeader.style.top = "0px";
      scrollHeader.style.height = "104px";
      scrollHeader.style.border = "none";
      scrollHeader.style.transition = "none";
      openedMenu.style.position = "fixed";
      openedMenu.style.top = "104px";
    }
  } else {
    scrollHeader.style.top = "-15px";
    scrollHeader.style.height = "0px";
    openedMenu.style.position = "absolute";
  }
  if (document.documentElement.scrollTop > firstScreen.offsetHeight-100) {
    about.style.transform = 'rotate(0deg)';
    about.style.opacity = "1";
  }
  if (document.documentElement.scrollTop < firstScreen.offsetHeight+200) {
    backToTop.style.display = "none";

  } else if (document.documentElement.scrollTop < firstScreen.offsetHeight+restOfPage.offsetHeight-450) {
    backToTop.style.color = "black";
    backToTop.style.display = "block";

  } else {
    backToTop.style.color = "white";

  }
  if (document.documentElement.scrollTop < firstScreen.offsetHeight+restOfPage.offsetHeight-100) {
    smSideBar.style.display = "block";
  } else {
    smSideBar.style.display = "none";
  }
}


var lists = document.querySelectorAll(".career-list");
var careerBtns = document.querySelectorAll(".career-button");
var ul = document.getElementsByTagName("ul")

lists[0].style.height = 'auto';
lists[0].style.margin = '20px 0px 20px 30px';
careerBtns[0].innerHTML = "-";

function controlList(elem) {
    var thisList = elem.nextElementSibling;
    if (thisList.offsetHeight == 0) {
        for (var i = 0; i < lists.length; i++) {
          if (lists[i] == thisList) {
            thisList.style.height = 'auto';
            thisList.style.margin = '20px 0px 20px 30px';
            elem.children[1].innerHTML = "-";
          } else {
            lists[i].style.height = 0;
            lists[i].style.margin = 0;
            careerBtns[i].innerHTML = "+";
          }
        }
    } else {
        thisList.style.height = 0;
        thisList.style.margin = 0;
        elem.children[1].innerHTML = "+";
    }
}

function getColoredItself(img) {
  img.style.filter = "grayscale(0)";
}

function getBlackWhiteItself(img) {
  img.style.filter = "grayscale(1)";
}

function getColored(button) {
  button.parentElement.firstElementChild.firstElementChild.style.filter = "grayscale(0)";
}

function getBlackWhite(button) {
  button.parentElement.firstElementChild.firstElementChild.style.filter = "grayscale(1)";
}
