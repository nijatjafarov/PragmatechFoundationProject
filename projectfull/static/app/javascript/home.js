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
var slide_imgs = firstScreen.getElementsByTagName("img");
var restOfPage = document.querySelector(".rest-of-page");
var smSideBar = document.querySelector(".sm-sidebar")
var open = false;
var currentImg = 0;

firstScreen.style.height = window.innerHeight - 105 + "px";

if(slide_imgs.length < 2) {
  document.querySelector(".corner-buttons").style.display = none;
}

for(var i = 0; i < slide_imgs.length; i++) {
  slide_imgs[i].style.zIndex -= i;
  slide_imgs[i].style.opacity = "0";
}
slide_imgs[0].style.opacity = "1";

function changeNext(){
  for(var i = 0; i < slide_imgs.length; i++) {
    slide_imgs[i].style.opacity = "0";
  };
  if(currentImg == slide_imgs.length-1) {
    currentImg = 0;
  } else {
    currentImg += 1;
  }
  setTimeout(function(){
    //firstScreen.firstElementChild.setAttribute("src", `img/first0${currentImg+1}.jpeg`);
    slide_imgs[currentImg].style.opacity = "1";
  }, 800);
}

function changePrev(){
  if(currentImg == 0) {
    currentImg = slide_imgs.length-1;
  } else {
    currentImg -= 1;
  }
  for(var i = 0; i < slide_imgs.length; i++) {
    slide_imgs[i].style.opacity = "0";
  };
  setTimeout(function(){
    //firstScreen.firstElementChild.setAttribute("src", `img/first0${currentImg+1}.jpeg`);
    slide_imgs[currentImg].style.opacity = "1";
  }, 800);
}

var workSquares = document.querySelectorAll(".work-square");
var squares = document.querySelectorAll(".square");
for( var i = 0; i < squares.length; i++) {
  squares[i].style.height = squares[i].clientWidth + "px";
}
for( var i = 0; i < workSquares.length; i++) {
  workSquares[i].style.height = workSquares[i].clientWidth - 20 + "px";
}

openedMenu.style.width = document.body.offsetWidth-100 + "px";

window.addEventListener('resize', dynamicSizes, false);

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


var a = 0;
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
  var oTop = $('#info').offset().top - window.innerHeight;
  if (a == 0 && $(window).scrollTop() > oTop) {
    $('.animated-value').each(function() {
      var $this = $(this),
        countTo = $this.attr('data-count');
      $({
        countNum: $this.text()
      }).animate({
          countNum: countTo
        },

        {

          duration: 1000,
          easing: 'swing',
          step: function() {
            $this.text(Math.floor(this.countNum));
          },
          complete: function() {
            $this.text(this.countNum);
            //alert('finished');
          }

        });
    });
    a = 1;
  }
});


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

var lists = document.querySelectorAll(".career-list");
var careerBtns = document.querySelectorAll(".career-button");

if (careerBtns.length == 1) {
  careerBtns[0].style.display = "none";
  careerBtns[0].parentElement.style.cursor = "auto"
}

listHeights = []

for (var i = 0; i < lists.length; i++) {
  listHeights.push(lists[i].offsetHeight + "px");
  lists[i].style.height = "0px";
}

lists[0].style.height = listHeights[0];
lists[0].style.margin = '40px 0px';
careerBtns[0].innerHTML = "-";

if (careerBtns.length != 1) {
  function controlList(elem) {
    var thisList = elem.nextElementSibling;
    if (thisList.offsetHeight == 0) {
        for (var i = 0; i < lists.length; i++) {
          if (lists[i] == thisList) {
            thisList.style.height = listHeights[i];
            thisList.style.margin = '40px 0px';
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
