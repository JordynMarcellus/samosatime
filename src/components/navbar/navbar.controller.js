'use strict';

angular.module('samosatime')
  .controller('NavbarCtrl', function ($scope) {
    $scope.date = new Date();
  });
