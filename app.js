var itemUrl = '/update_items'
var donorUrl = 'http://127.0.0.1:5000/get_donors/'
var categoryUrl = 'http://127.0.0.1:5000/get_categories/'
var taxLetterUrl = 'http://127.0.0.1:5000/get_tax_letter_url/'
var app = angular.module('createItem', ['ngRoute']);

app.config(function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'partials/donors.html',
      controller: 'donorController'
    })
    .when('/category', {
      templateUrl: 'partials/category.html',
      controller: 'categoryController'
    })
    .when('/price', {
      templateUrl: 'partials/price.html',
      controller: 'mainController'
    })
    // .when('/manage', {
    //   templateUrl: 'partials/manage.html',
    //   controller: 'managementController'
    // })
    .otherwise({redirectTo: '/'});
    $locationProvider.html5Mode(true);
});

app.service('itemCreater', function($http) {
  this.newItem = {};
  this.pushItem = function($http) {
    $http.post(itemUrl, newItem).then(function() {
      console.log('item sucessfully added') //debugging
    }, function() {
      console.log('there was an error adding the item') //debugging
    })
  }
});

app.controller('donorController', function($scope, $location, $http, itemCreater, $window) {
  $scope.donors = [];
  $scope.donorSearch = function() {
    if ($scope.donorName) {
      $http.get(donorUrl + $scope.donorName, {responseType: "json"}).then(function(response) {
        // console.log('searched'); debug
        // console.log(response.data.donors); debug
        $scope.donors = response.data.donors;
      });
    } else {
      $scope.donors = [];
    };
  };
  $scope.donorClick = function(donorId) {
    popUp = document.getElementsByClassName('modal')[0];
    popUp.style.display = 'initial';
    $scope.close = function() {
      popUp.style.display = 'none';
    }
    $scope.createitem = function() {
      itemCreater.newItem.donor = donorId;
      $location.path('/category')
    }
    $scope.taxletter = function() {
      $http.get(taxLetterUrl + donorId, {responseType: "text"}).then(function(response) {
        $window.location = response.data;
      })
    }
  }
});

app.service('loadCategories', function($http) {
  this.load = function(parentId) {
    return $http.get(categoryUrl + parentId, {responseType: "json"}).then(function(response) {
      return response.data
    });
  }
});

app.controller('categoryController', function($scope, loadCategories, $location, itemCreater) {
  var categoryList = [];
  loadCategories.load('0').then(function(data) {
    $scope.categories = data.categories;
    // console.log($scope.categories);
  });
  $scope.categoryClick = function(parentId) {
    categoryList.push(parentId);
    loadCategories.load(parentId).then(function(data) {
      if (data.categories.length > 0) {
        $scope.categories = data.categories;
      } else {
        itemCreater.newItem.categories = categoryList;
        console.log(itemCreater.newItem);
        $location.path('/');
      };
    })
  }
});
