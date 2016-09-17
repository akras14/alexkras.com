(function () {
    function getRandomInt(max) {
        if(typeof max === "undefined" ) throw new Error("Max is required");
        max = Math.floor(max);
        return Math.floor(Math.random() * max);
    }
    function getDayAndMonth(birthday) {
        return birthday.split(" ").splice(0, 2).join(" ")
    }
    function getRandomSample(numToSample){
        var bdCount = birthdayData.length;
        var randomActors = [];
        for(var i = 0; i < numToSample; i++){
            var bdId = getRandomInt(bdCount);
            var bd = birthdayData[bdId];
            randomActors.push(bd);
        }
        return randomActors;
    }
    var birthdayData = [];
    var vm;
    function setUpView(){
        vm = new Vue({
            el: '#app',
            data: {
                birthdays: getRandomSample(15),
                sampleSize: null
            },
            beforeCompile: function(){
                
            },
            methods: {
                reSample: function(){
                    var sampleSize = Number.parseInt(vm.sampleSize, 10);
                    vm.$set('birthdays', getRandomSample(sampleSize)); 
                }
            }
        });
    }
    setTimeout(function(){
        fetch("birthdays-smaller.json")
                    .then(res => res.json())
                    .then(json => birthdayData = json)
                    .then(setUpView)
                    .then(() => vm.reSample());
    }, 100)    
})();