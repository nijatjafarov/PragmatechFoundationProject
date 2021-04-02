
var todo = document.querySelector('.todo');

var inputBtn = document.querySelector("#plus"); //funksiya icinde islemir
var open = true;

function addBlock() {

  var input = document.getElementsByTagName('input')[0];
  var single=`
  <div class="output">
    <p onclick='showOnly(this)'>${input.value}</p>
    <button class="button" id="minus" onclick='removeBlock(this)'>-</button>
  </div>
  `
    todo.innerHTML += single;
}


function removeBlock(element){
    todo.removeChild(element.parentElement);
}

function showOnly(eleBunu) {
  var inputPart = document.querySelector(".input");
  if(open) {
    for (var i = 1; i < todo.children.length; i++) {
      todo.children[i].style.display = 'none';
    }
    inputPart.children[0].disabled = true;
    inputPart.children[0].placeholder = "Seçdiyindən vaz keçmədən yazmaq və əlavə etmək olmaz";
    inputPart.children[1].disabled = true;
    inputPart.children[1].style.cursor = 'auto';
    eleBunu.nextElementSibling.style.display = 'none';
    open = false;
  } else {
    for (var i = 1; i < todo.children.length; i++) {
      todo.children[i].style.display = 'flex';
    }
    inputPart.children[0].disabled = false;
    inputPart.children[0].placeholder = "İndi yenə kölnündən keçəni yaza bilərsən";
    inputPart.children[1].disabled = false;
    inputPart.children[1].style.cursor = 'pointer';
    eleBunu.nextElementSibling.style.display = 'block';
    open = true;
  }

  eleBunu.parentElement.style.display = 'flex';
}
