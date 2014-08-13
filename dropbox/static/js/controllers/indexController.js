function indexController($scope, $http) {

//    $http.post('/check_login/').success(function(successResponse) {
//        console.log(successResponse);
//        var user = successResponse;
//    }).error(function(errorResponse) {
//            console.log(errorResponse);
//        });


	$scope.toggleSettings = function() {
		$scope.showSettings = !$scope.showSettings;
	};

	console.log("indexController");
//    var loggedInUserId = Auth.user;
//    console.log(user.username);

    $http.get('/api/v1/media/?owner='+$scope.user+'&api_key=special-key/').success(function(successResponse) {
//    $http.get('/api/v1/media/').success(function(successResponse) {
        console.log(successResponse);
        $scope.all_media = successResponse;
    }).error(function(errorResponse) {
            console.log(errorResponse);
        });
}
