var initialLocation;
var browserSupportFlag =  new Boolean();
var map;
var infowindow = new google.maps.InfoWindow();
  
function gMapInitialize() {
  var myOptions = {
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: true
  };

  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  
  // Try W3C Geolocation method (Preferred)
  if(navigator.geolocation) {
    browserSupportFlag = true;
    navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
      map.setCenter(initialLocation);
      
    }, function() {
      handleNoGeolocation(browserSupportFlag);
    });
  } else if (google.gears) {
    // Try Google Gears Geolocation
    browserSupportFlag = true;
    var geo = google.gears.factory.create('beta.geolocation');
    geo.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.latitude,position.longitude);
      //showContentOnMap("Location found using Google Gears", initialLocation);
      map.setCenter(initialLocation);
      
    }, function() {
      handleNoGeolocation(browserSupportFlag);
    });
  } else {
    // Browser doesn't support Geolocation
    browserSupportFlag = false;
    handleNoGeolocation(browserSupportFlag);
  }
  
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag == true) {
	  alert("geolocation service failed");
  } else {
	  alert("Browser does not support geolocation");
  }
 
  
}


function showContentOnMap(contentString, location) {	
	var marker = new google.maps.Marker({
        position: location, 
        map: map, 
        title:contentString
    });   
}


function fillMap() { 
	
	makeRequest("getUsers?lat=" + initialLocation.lat() + "&lon=" + initialLocation.lng(), 
				"GET", "", "", fillUserList); 
	
 	
}

function fillUserList(response){

	for(var i in response){
		userLocation = new google.maps.LatLng(response[i][1],response[i][2]);
		showContentOnMap(response[i][0], userLocation);
	}
		
		
	
	
}

