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
var backToTop = document.querySelector(".back-to-top");

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
    if (document.documentElement.scrollTop < 100) {
      backToTop.style.display = "none";
  
    } else if (document.documentElement.scrollTop < document.body.offsetHeight - document.querySelector(".footer").offsetHeight - 450) {
      backToTop.style.color = "black";
      backToTop.style.display = "block";
  
    } else {
      backToTop.style.color = "white";
  
    }
});



// Filter underline
var categories = document.querySelector(".categories");
var filter_links = categories.getElementsByTagName("a");

function underline(link) {
    link.style.textDecoration = "underline";
}

function deleteline(link) {
    link.style.textDecoration = "none";
}


// On resize
openedMenu.style.width = document.body.offsetWidth-100 + "px";

window.addEventListener('resize', openedMenuWidth, false);

function openedMenuWidth() {
  openedMenu.style.width = document.body.offsetWidth-100 + "px";
}

//Back to Top ucun ogurluq kod. Canim ucun jQuery bilmemekdendir
$(document).ready(function(){
  // Add smooth scrolling to all links
  $(".back-to-top").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: 0
      }, 100, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});


var portItems = document.querySelectorAll(".port-item");
var portButton = document.querySelector(".port-button");
var turn = 5; 

for (var i = 0; i < 5; i++) {
  if (portItems[i]) {
    console.log("firs loop")
    portItems[i].style.display = "block";
  }
}

if (portItems.length <= 5) {
  portButton.style.display = "none";
}

function loadMore(){
  for (var i = turn; i < turn + 5; i++) {
    if (portItems[i]){
      console.log(portItems[i])
      portItems[i].style.display = "block";
      if (i == portItems.length-1) {
        {"button"}
      portButton.style.display = "none";
      break
      }
    } else {
      {"button"}
      portButton.style.display = "none";
      break
    }
  }
  turn += 4;
}