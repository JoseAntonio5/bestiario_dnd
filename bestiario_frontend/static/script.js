let vida_min = document.getElementById('vida_min')
let vida_max = document.getElementById('vida_max')
let btn = document.getElementById('display_vida_btn')

let display_vida = document.querySelector('#display_vida')

function vidaMonstro(min, max) {
    num = Math.floor(Math.random() * (max - min) + min)
    console.log(num)
    return num
}

btn.addEventListener('click', () => {
    display_vida.innerText = vidaMonstro(vida_min, vida_max)
    console.log(vidaMonstro(vida_min, vida_max))
});