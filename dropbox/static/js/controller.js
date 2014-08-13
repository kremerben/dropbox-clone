



















///////////////////////////////////////////


theaterPlus.controller('allMovies', function($scope, $http, MovieService) {

	$scope.getUpcomingMovies = function () {
		MovieService.getMovies('upcoming', $scope.searchTerms, MovieService.searchCountry, function(data) {
			$scope.movies = data.movies;
			console.log(data);
		});
	};
	

	$scope.getCurrentMovies = function () {
		MovieService.getMovies('in_theaters', $scope.searchTerms, MovieService.searchCountry, function(data) {
			$scope.movies = data.movies;
			console.log(data);
		});
	};


	$scope.searchMovies = function () {
		MovieService.searchMovie($scope.movieSearch, MovieService.searchCountry, 12, function(data) {
			$scope.movies = data.movies;
			console.log(data);
		});
	};
	
	$scope.showResults = true;
	
	
	
	
	
	
	$scope.moreInfo = function(index) {
		$scope.movies[index].showInfo = true;
	};
	$scope.hideInfo = function(index) {
		$scope.movies[index].showInfo = false;
	};
	
	$scope.showSettings = false;
	$scope.toggleSettings = function() {
		$scope.showSettings = !$scope.showSettings;
	};
	
});



theaterPlus.controller('similar', function($scope, $http, MovieService) {

	$scope.showSimilar = function () {
		MovieService.getSimilar($scope.similarSearch, MovieService.searchCountry, MovieService, function(data) {
			$scope.similarMovies = data.movies;
			console.log(data);
		});
	};
	
	$scope.showSimilarResults = true;

	$scope.moreInfo = function(index) {
		$scope.similarMovies[index].showInfo = true;
	};
	$scope.hideInfo = function(index) {
		$scope.similarMovies[index].showInfo = false;
	};
	
	$scope.showSettings = false;
	$scope.toggleSettings = function() {
		$scope.showSettings = !$scope.showSettings;
	};


});




theaterPlus.controller('userControls', function($scope, $http, MovieService) {
	MovieService.searchCountry = $scope.searchCountry;

/*
	$scope.searchMovies = function () {
		MovieService.getSimilar($scope.similarSearch, $scope.searchCountry, 12, function(data) {
			$scope.similarMovies = data.movies;
			console.log(data);
		});
	};
	
	$scope.showSimilarResults = true;
*/

});


//////////////////////////////////////////////




theaterPlus.controller('movieRequest', function($scope, $http) {
	$scope.getMovies = function () {

		$http.jsonp(
		 'http://api.rottentomatoes.com/api/public/v1.0/movies', {
		 params: {
		     apikey: '88a8qpv9kwg657jxb97ma5nn',
		     q: $scope.searchTerms,
		     page_limit: '10',
		     callback: 'JSON_CALLBACK'
		 }
		}).then(function(promise) {
		    $scope.movies;
		     for (var i = 0; i < promise.data.movies.length; i++) {
		     	$scope.movies = promise.data.movies;
		         
		     }
		     $scope.showResults = true;
		 });	
/* 		 console.log($scope.movies); */
	}
	$scope.moreInfo = function(index) {
		$scope.movies[index].showImage = true;
	};
	$scope.hideInfo = function(index) {
		$scope.movies[index].showImage = false;
	};
});

//////////////////////////////////////////////


theaterPlus.controller("myCtrl3", function($scope) {
    $scope.list = ['Learn Angular'];
	$scope.addToList = function() {
        if ($scope.todo !== '') {
            $scope.list.push($scope.todo);
            $scope.todo = '';
        }
	};
});




theaterPlus.controller("faveBooks", function($scope) {
    $scope.faveList = [{
  "title": "James and the Giant Peach",
  "author": "James",
  "description": "the giant peach",
  "genre": "children"
},{
  "title": "Into the Wild",
  "author": "I Forgot",
  "description": "Going out for a walk",
  "genre": "travel"
}  ];
	$scope.addBookToList = function() {
        if ($scope.book !== '') {
            $scope.faveList.push($scope.book);
            $scope.book = '';
			if ($scope.faveList.length > 5) {
				$scope.showBookMessage = true;
			}
        }
	};
	$scope.moreInfo = function(index) {
		$scope.faveList[index].showDesc = true;
	};
	$scope.hideInfo = function(index) {
		$scope.faveList[index].showDesc = false;
	};
});





theaterPlus.controller("registration", function($scope) {
	$scope.users = [];
	$scope.register = function() {
		$scope.regComplete = true;
		$scope.users.push($scope.user);
		
	};	
	$scope.newReg = function() {
		$scope.regComplete = false;
		$scope.user = {};
	};
});