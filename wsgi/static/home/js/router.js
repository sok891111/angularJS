(function(){
var path = view_path;
app = angular.module('app', ['ngRoute'])
.config(function ($routeProvider,$interpolateProvider) {
  //django & angularJs conflict
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');

  //router
  $routeProvider
  .when('/', {templateUrl: path+'/main.html', controller: 'mainCtrl'})
  .when('/message', {templateUrl: path+'/msg.html', controller: 'msgCtrl'})
  .otherwise({redirectTo: '/'});
  });

})();

/*.when('/userList', {templateUrl: '/views/userList.html', controller: 'userListCtrl'})
      .when('/user/:userId', {templateUrl: 'views/userDetail.html', controller: 'userDetailCtrl'})*/
    

