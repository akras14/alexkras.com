(function () {
    angular.module('birthdayApp', [])
        .component('birthdayApp', {
            templateUrl: 'birthday-app.component.html',
            controller: BirthdayAppController,
            controllerAs: "ba"
        });
    BirthdayAppController.$inject = ['$http'];
    function BirthdayAppController($http){
        var ba = this;
        ba.options = ["23", "70"];
        ba.selected = ba.options[0];
        ba.reSample = reSample;
        var birthdayData = [];
        $http.get("birthdays-smaller.json")
            .then(res => res.data)
            .then(json => birthdayData = json)
            .then(reSample);

        function reSample(){
            var sampleSize = Number.parseInt(ba.selected, 10);
            ba.birthdays = getRandomSample(birthdayData, sampleSize);
            ba.matches = getBirthdayMatch(ba.birthdays);
        }
    }
    function getRandomInt(max) {
        if(typeof max === "undefined" ) throw new Error("Max is required");
        max = Math.floor(max);
        return Math.floor(Math.random() * max);
    }
    function getDayAndMonth(birthday) {
        return birthday.split(" ").splice(0, 2).join(" ")
    }
    function getRandomSample(birthdayData, numToSample){
        var bdCount = birthdayData.length;
        var randomActors = [];
        for(var i = 0; i < numToSample; i++){
            var bdId = getRandomInt(bdCount);
            var bd = birthdayData[bdId];
            randomActors.push(bd);
        }
        return randomActors;
    }
    function getBirthdayMatch(birthdays){
        var matches = [];
        birthdays.forEach(bd => {
            var result = birthdays.filter(test => {
                return getDayAndMonth(bd.db) === getDayAndMonth(test.db);
            });
            if(result.length > 1) {
                matches = _.union(matches, result);
            }
        });
        return matches;
    }   
})();