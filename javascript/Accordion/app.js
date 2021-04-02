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
