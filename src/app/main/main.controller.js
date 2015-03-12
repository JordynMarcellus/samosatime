'use strict';

angular.module('samosatime')
  .controller('MainCtrl', function ($scope, $http) {
    $http.get('data/samosas.json').success(function(data){
      var samosas = data.samosas;
      var output = '<ul>';
      for(var i = 0; i < samosas.length; i++){
        output += '<li>' + samosas[i].name + '</li>';
      }
      output += '</ul>';

      console.log(output);
    })
  });
