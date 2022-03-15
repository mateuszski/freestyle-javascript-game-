initGame();

function initGame() {

    // Your game can start here, but define separate functions, don't write everything in here :)

}
let start = false
let hitCounter=0;
function changePosition() {
    let btn = document.getElementById('btn');

    if (start == true ) {
        btn.classList.add('target-button')
        btn.style.top = 50 + '%';
        btn.style.left = 50 + "%";
        btn.innerHTML = "Start game!"
        start = false
        hitCounter = 0
        console.log('dziala ')
    } else {
        btn.innerHTML = ""
        btn.classList.add('target-button')
        btn.classList.remove('target-button-start')
        btn.style.top = Math.floor((Math.random() * 750) + 1) + "px";
        btn.style.left = Math.floor((Math.random() * 900) + 1) + "px";
        hitCounter +=1;
    }
    return hitCounter
   /* return [hitCounter, shootCounter]; */
}
function onloadbutton() {
    let btn = document.getElementById('btn');
    btn.innerHTML = "Start game!"
}

let missCounter=0;
function countMiss(){
    missCounter+=1;
    return missCounter
}


function statistics(hitCounter, missCounter, maxTimer, userName) {
    let shootCounter=hitCounter+missCounter;
    let accuracy = hitCounter/shootCounter * 100;
    accuracy = accuracy.toString() + "%";
    let hitsPerSecond = hitCounter/maxTimer;
    hitsPerSecond = hitsPerSecond.toString() + "hit/s"
    document.getElementById("accuracy").innerHTML = accuracy;
    document.getElementById("miss_counter").innerHTML = missCounter;
    document.getElementById("hits_per_second").innerHTML = hitsPerSecond;
    document.getElementById("hit_counter").innerHTML = hitCounter;
    document.getElementById("user_name").innerHTML = userName;
}

function startButton() {

}