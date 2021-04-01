var lists = document.querySelectorAll(".career-list");
var careerBtns = document.querySelectorAll(".career-button");

lists[0].style.height = 'auto';
lists[0].style.margin = '20px 0px 20px 30px';
careerBtns[0].innerHTML = "-";

function controlList(elem) {
    var thisList = elem.parentElement.nextElementSibling;

    if (thisList.offsetHeight == 0) {
        for (var i = 0; i < lists.length; i++) {
            lists[i].style.height = 0;
            lists[i].style.margin = 0;
            careerBtns[i].innerHTML = "+";
        }

        thisList.style.height = 'auto';
        thisList.style.margin = '20px 0px 20px 30px';
        elem.innerHTML = "-";
    } else {
        thisList.style.height = 0;
        thisList.style.margin = 0;
        elem.innerHTML = "+";
    }
}
