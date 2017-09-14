var app = angular.module('myApp', ['ngMaterial']);

app.controller("ctrlMain", function($scope, $http) {
    console.log('ctrlMain loaded');

    apiUrl = '/Local_Dev_Example/api/';

    $scope.numbers = [1,2,3,4,5,6,7,8,9];

    $scope.number_two = undefined;
    $scope.number_one = undefined;

    $scope.currentTime = undefined;

    $scope.add = function() {
      url = apiUrl + 'addition?numone=' + $scope.number_one + '&numtwo=' + $scope.number_two;
      getData(url,  'add');
    }

    $scope.getTime = function() {
      url = apiUrl + 'time';
      getData(url, 'time');
    }

    var getData = function (url, type) {
      console.log(url);
      $http.get(url)
      .then(function(res){
        console.log('res:' , res);
        if (type=='time') {
          $scope.currentTime = res.data['time_str'];
        } else {
          $scope.add_result = res.data['output'];
        }
      });
    }

});
