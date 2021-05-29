// Navbar Highlighter
var navbar = document.querySelector(".navbar");
var navbarSections = navbar.getElementsByTagName("li");
var highlighter = document.querySelector(".highlighter");

function highlight(num) {
    highlighter.style.width = navbarSections[num].offsetWidth + "px";
    var navPos = 0;
    for (var i = 0; i < num; i++) {
      navPos += navbarSections[i].offsetWidth;
    }
    highlighter.style.left = navPos + "px";
  }


// Opened menu
var openedMenu = document.querySelector(".opened-menu");
var header = document.querySelector(".header")
open = false;
function openCloseMenu() {
    if(open) {
      openedMenu.style.height = "0";
      openedMenu.style.border = "none";
      header.style.borderBottom = "1px solid #ebebeb";
      open = false;
    } else {
      openedMenu.style.height = "193px";
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


// On Scroll
var scrollHeader = document.querySelector(".scroll");

$(window).scroll(function() {
    if (document.documentElement.scrollTop > 114) {
      if (openedMenu.offsetHeight != 0) {
        scrollHeader.style.top = "0px";
        scrollHeader.style.height = "104px";
        scrollHeader.style.border = "none";
        scrollHeader.style.transition = "none";
        openedMenu.style.position = "fixed";
        openedMenu.style.top = "104px";
      } else {
        scrollHeader.style.borderBottom = "1px solid #ebebeb";
      }
    } else {
      scrollHeader.style.top = "-15px";
      scrollHeader.style.height = "0px";
      openedMenu.style.position = "absolute";
    }
});


// On resize
openedMenu.style.width = document.body.offsetWidth-100 + "px";

window.addEventListener('resize', openedMenuWidth, false);

function openedMenuWidth() {
  openedMenu.style.width = document.body.offsetWidth-100 + "px";
}


//Image height-wight balance
var contactImg = document.querySelector(".contact-img");
contactImg.style.height = contactImg.offsetWidth*0.5 + "px";

window.addEventListener('resize', contactImgSize, false);

function contactImgSize() {
  contactImg.style.height = contactImg.offsetWidth*0.5 + "px";
}
