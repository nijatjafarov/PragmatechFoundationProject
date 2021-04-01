
var todo = document.querySelector('.todo');
var inputPart = document.querySelector(".input");

function addBlock() {
  var input = document.getElementsByTagName('input')[0].value;

  var single=`
  <div class="output">
    <p>${input}</p>
    <button class="button" id="minus" onclick='removeBlock(this)'>-</button>
  </div>
  `
    todo.innerHTML += single;
}

function removeBlock(element){
    todo.removeChild(element.parentElement);
}
