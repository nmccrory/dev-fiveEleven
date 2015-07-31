app.config(function ($routeProvider) {
  console.log('here');
  $routeProvider
    .when('/',{
        templateUrl: 'static/mapvisuals/partials/map.html',
        controller: "MapController",
        controllerAs: "map"
    })
    .when('/piechart',{
    	templateUrl: 'static/mapvisuals/partials/pieChart.html',
    	controller: "PieChartController",
    	controllerAs: "pie"
    })
    .otherwise({
        redirectTo: '/',
    });
});