var dropboxPlus = angular.module('dropboxPlus', ['ngRoute','ngResource']);

dropboxPlus.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', { templateUrl: '/static/js/views/index.html', controller: 'indexController' });
}]);
