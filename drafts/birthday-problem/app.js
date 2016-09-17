var birthdayData = [];
fetch("birthdays-smaller.json")
    .then(res => res.json())
    .then(json => birthdayData = json)
    .then(() => onDataLoad());
function getRandomInt(max) {
    if(!max) throw new Error("Max is required");
    max = Math.floor(max);
    return Math.floor(Math.random() * max);
}
function getDayAndMonth(birthday) {
    return birthday.split(" ").splice(0, 2).join(" ")
}
function onDataLoad() {
    var bdCount = birthdayData.length;
    var numToSample = 15;
    var selected = [];
    for(var i = 0; i < numToSample; i++){
        var bdId = getRandomInt(bdCount);
        var bd = birthdayData[bdId];
        selected.push(bd);
    }
    console.log(selected);
    new Vue({
        el: '#app',
        data: {
            birthdays: selected
        }
    });
}