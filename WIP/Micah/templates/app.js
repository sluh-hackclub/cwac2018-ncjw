var ncjw = angular.module('ncjw-app', [ 'ngRoute' ]);

		ncjw.config(function($routeProvider) {
		    $routeProvider
		    .when("/", {
		        templateUrl : "home.html"
		    })
		    .when("/donor_search", {
		        templateUrl : "donor_search.html"
		    })
		    .when("/itemize/:cid", {
		        templateUrl : "itemize.html",
				controller:"itemizeCtrl"
		
		    })
		    .when("/add_price", {
		        templateUrl : "add_price.html"
		    });
		});
		
		
		ncjw.controller('itemizeCtrl', function($scope, $http, $templateCache,$routeParams,$location,$route) {
							$scope.currentTier=0;
							$scope.$route = $route;
							$scope.data=[];
							$scope.selected=[];
							$scope.prices=[];
							$scope.pricesLoaded=false;
							$scope.selectedl=null;
								$scope.$routeParams = $routeParams;
								$scope.$location = $location;
								//$scope.tier3_selections=[]
							$scope.loadCategories=function(){
								$http({
												method : 'GET',
												url : 'http://localhost:3000/api/getIData/'+$scope.$routeParams.cid,
												headers : {
													'Content-Type' : 'application/json'
												}
											})	.then(function (res){
													$scope.data=res.data;
													console.log(res.data);
													if($scope.data.length>0){
														$scope.currentTier=$scope.data[0].tier;
													}
												   },function (error){

												   });
							
							$http({
											method : 'GET',
											url : 'http://localhost:3000/api/getParent/'+$scope.$routeParams.cid,
											headers : {
												'Content-Type' : 'application/json'
											}
										}).then(function (res){
											if(res.data.length>0){
												$scope.parent=res.data[0].parentId;
											}
											
											
											},function (error){});
							};
							$scope.loadCategories();
							
							// $scope.add_prices=function(){
							// 								console.log($scope.tier3_selections[0]);
							// 							}
							
							
							$scope.add_price = function(){
								
							    $scope.cIdArray = [];
							   	 angular.forEach($scope.data, function(d){
							   	
							   	if (d.selected) $scope.cIdArray.push(d.id);
							   	});
							console.log($scope.cIdArray);
							$http({
											method : 'GET',
											url : 'http://localhost:3000/api/getPrices/'+$scope.cIdArray,
											headers : {
												'Content-Type' : 'application/json'
											}
										}).then(function (res){
											if(res.data.length>0){
												$scope.pricesLoaded=true;
											$scope.prices.push(res.data[0].price1);
											$scope.prices.push(res.data[0].price2);
											$scope.prices.push(res.data[0].price3);
											$scope.prices.push("");
										}
											
											
											},function (error){});
							
							   	//window.location.href = "#!add_price/"+$scope.$routeParams.cid+","+$scope.cIdArray
							  }
					
					
					
					
				});