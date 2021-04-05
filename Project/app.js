//Ana sehife Accordion
// var lists = document.querySelectorAll(".career-list");
// var careerBtns = document.querySelectorAll(".career-button");
// var ul = document.getElementsByTagName("ul")

// lists[0].style.height = 'auto';
// lists[0].style.margin = '20px 0px 20px 30px';
// careerBtns[0].innerHTML = "-";

// function controlList(elem) {
//     var thisList = elem.nextElementSibling;
//     if (thisList.offsetHeight == 0) {
//         for (var i = 0; i < lists.length; i++) {
//           if (lists[i] == thisList) {
//             thisList.style.height = 'auto';
//             thisList.style.margin = '20px 0px 20px 30px';
//             elem.children[1].innerHTML = "-";
//           } else {
//             lists[i].style.height = 0;
//             lists[i].style.margin = 0;
//             careerBtns[i].innerHTML = "+";
//           }
//         }
//     } else {
//         thisList.style.height = 0;
//         thisList.style.margin = 0;
//         elem.children[1].innerHTML = "+";
//     }
// }

//design-project sehifesi uzerinden islemisem
console.log("salam")
var header = document.querySelector(".header")
var navbar = document.querySelector(".navbar");
var navbarSections = navbar.getElementsByTagName("li");
var highlighter = document.querySelector(".highlighter");
var scrollHeader = document.querySelector(".scroll");
var scrollSections = scrollHeader.getElementsByTagName("li");
var scrollHighlighter = scrollHeader.querySelector(".highlighter");
var hamburgerMenu = document.querySelector(".hamburger-menu");
var openedMenu = document.querySelector(".opened-menu");
var open = false;

openedMenu.style.width = document.body.offsetWidth-100 + "px";

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

var scrollTillFooter = document.querySelector(".project-page-inside").offsetHeight;
var mainProjectHeight = document.querySelector(".main-project").offsetHeight;
// Ana sehife about section
// var about = document.querySelector('.about');

var backToTop = document.querySelector(".back-to-top");
var next_previous = document.querySelectorAll(".next-previous")

window.onscroll = function() {scroll()};

function scroll() {
  if (document.documentElement.scrollTop > 114) {
    if (openedMenu.offsetHeight == 0) {
      scrollHeader.style.top = "0px";
      scrollHeader.style.height = "70px";
      scrollHeader.style.borderBottom = "1px solid #ebebeb";

    } else {
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
  // if (document.documentElement.scrollTop > 700) {
  //   bu.style.transform = 'rotate(0deg)';
  //   bu.style.opacity = "1";
  // }
  if (document.documentElement.scrollTop < 1000) {
    backToTop.style.display = "none";

  } else if (document.documentElement.scrollTop < scrollTillFooter-600) {
    backToTop.style.color = "black";
    backToTop.style.display = "block";
  } else {
    backToTop.style.color = "white";
  }
  if (document.documentElement.scrollTop > mainProjectHeight-350) {
    next_previous[0].style.opacity = "0";
    next_previous[1].style.opacity = "0";
  } else {
    next_previous[0].style.opacity = "1";
    next_previous[1].style.opacity = "1";
  }
}

// Portfolio item sehifesi clickleyende acilan hal




var background = document.querySelector(".background");
var slider = document.querySelector(".slider");
var arrows = document.querySelector(".arrows");
var slide = document.querySelector(".slide");
var imgs = document.querySelectorAll(".img");
var pageInfo = document.querySelector("#page-info");
var expandIcon = document.querySelector("#expand-icon");
var currentSlide;

background.style.height = document.body.offsetHeight + 'px';
// function hideBackground(bckgrnd) {
//   bckgrnd.style.opacity = "0";
// }

function showImg(index) {
  currentSlide = index;
  pageInfo.children[0].innerHTML = currentSlide;
  //slide.replaceChild(imgs[currentSlide-1].firstElementChild, slide.firstElementChild)
  slide.firstElementChild.setAttribute("src", `img/design-project0${currentSlide}.jpeg`);
  background.style.display = "block"
}

// background.addEventListener("click", function() {
//   background.style.display = "none";
// })

function showBtns() {
  arrows.style.opacity = "1";
}

function hideBtns() {
  arrows.style.opacity = "0";
}

function changeNext() {
  if (currentSlide == imgs.length) {
    currentSlide = 1;
  }else {
    currentSlide += 1;
  }
  slider.style.opacity = "0";
  setTimeout(function(){
    slider.style.opacity = "1";
    pageInfo.children[0].innerHTML = currentSlide;
    slide.firstElementChild.setAttribute("src", `img/design-project0${currentSlide}.jpeg`);
   }, 600);
}

function changeBefore() {
  if (currentSlide == 1) {
    currentSlide = imgs.length;
  }else {
    currentSlide -= 1;
  }
  slider.style.opacity = "0";

  setTimeout(function(){
    slider.style.opacity = "1";
    pageInfo.children[0].innerHTML = currentSlide;
    slide.firstElementChild.setAttribute("src", `img/design-project0${currentSlide}.jpeg`);
  }, 600);
}

pageInfo.children[1].innerHTML = imgs.length;

expandIcon.addEventListener("click", function() {
  slider.style.width = "1200px";
  arrows.style.width = "1200px";
})
