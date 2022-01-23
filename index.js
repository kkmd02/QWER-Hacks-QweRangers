// me learning

// typeof ___ returns "string", "object", etc

var list = [1,2,3];
var tb_input = document.getElementById('textBoxId');
var button = document.getElementById('Search_button');

tb_input.onchange = function(){
    console.log(tb_input.value);
}
button.onclick = function(){
    console.log(button)
    fetch('http://localhost:5000/about', {
        'method': 'POST',
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Accept': 'application/json',
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url,
    'body': JSON.stringify({
            company:tb_input.value
        })
    })
    .then((data)=>{return data.json()})
    .then((data)=>{
        console.log(data)
        var score = document.getElementById('score')
        score.innerHTML = data['score']
        var answer_box = document.getElementById('answer_box')
        answer_box.innerHTML = data['output']
        var queer_owned = document.getElementById('queer_owned')
        queer_owned.innerHTML = data['queer']
        
    })
}


