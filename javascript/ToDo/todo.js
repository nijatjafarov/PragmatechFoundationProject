
let todo=document.querySelector('.todo')
let single=`
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="Kategoriya..">
                        <div class="input-group-append">
                            <span class="input-group-text" id="plus" onclick='addBlock()'>+</span>
                            <span class="input-group-text" id="minus" onclick='removeBlock(this)'>-</span>
                        </div>
                    </div>
`

let content=single;


function addBlock(){
    content+=single
    todo.innerHTML=content;
}

function removeBlock(elem){
    if (content != single) {
        content = content.replace(single, "")
        todo.innerHTML=content;
    }
}
