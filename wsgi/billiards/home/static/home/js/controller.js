(function(){

  if(!app) return;
  //mainCtrl
  app.controller('mainCtrl'
    ,['$scope','$http','$routeParams','$location'
    ,function($scope, $http, $routeParams, $location) {

      //테스트용 임시 true
      $scope.hasMessage = true;

      //테스트용 임시 true
      $scope.hasPlay = true;

      $scope.user ={
        "id" : "sok891111",
        "point" : 200,
        "deptRank" : 2,
        "uniRank" : 4,
        "lastPlay" : "2015-04-23",
        "totalUserCnt" : 4000
      }

      $scope.notices = [
        "테스트 공지사항",
        "현재 게임 진행 중",
          "테스트 공지사항",
        "현재 게임 진행 중",
          "테스트 공지사항",
        "현재 게임 진행 중",
          "테스트 공지사항",
        "현재 게임 진행 중",
          "테스트 공지사항",
        "현재 게임 진행 중",
          "테스트 공지사항",
        "현재 게임 진행 중",
        "하하호호"
      ]
     

  }]);

  //msgCtrl
  app.controller('msgCtrl'
    ,['$scope','$http','$routeParams','$location','$route','msgFactory'
    ,function($scope, $http, $routeParams, $location , $route, msgFactory) {

      //retrieve messageList
      msgFactory.getMessageList().
      success(function(data, status) {
        $scope.messages= JSON.parse(data)
      });


      $('#test').click(function(){
      //create message
      var data = $('#msgForm').serializeObject();
      msgFactory.createMessage(data).
        success(function(data, status) {
          $('#sendMsgModal').modal('hide');
          $('#msgForm')[0].reset();
          $route.reload();
        });  
      });
      

      

      //filter
      $scope.challenge = function(item){
        return item.msg_type == 'chn'
      }     
      $scope.normal = function(item){
        return item.msg_type == 'nor'
      }     

      $scope.setModalMsg =function(message,type){
        $scope.modalMsg= message;
        $scope.modalType= type;
      }

  }]);


})();
