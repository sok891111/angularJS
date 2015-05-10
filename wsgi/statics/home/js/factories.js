(function(){
	if(!app) return;
	app.factory('msgFactory', function($http){

	    var factory = {};
	    var csrftoken = getCookie('csrftoken');
	    factory.getMessageList = function(){
	    	 var req = {
				method: 'POST',
				url: '/message/retrieveMessage/',
				headers: {
					"X-CSRFToken": csrftoken
				},data : {
					"" : ""
				}
			}
	       return $http(req);
	    };

	    factory.createMessage = function(data){
	    	 var req = {
				method: 'POST',
				url: '/message/createMessage/',
				headers: {
					"X-CSRFToken": csrftoken
				},data : data
				
				}
	       return $http(req);
	    };

	    return factory;

	});

})();