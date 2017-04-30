
function positionFound(position) {
	// document.getElementById('lat').value = position.coords.latitude;
	// document.getElementById('long').value = position.coords.longitude;
	drawMap();
}

// creates the map based on user's browser location 
function drawMap() {
	var mapCanvas = document.getElementById('google_map');
	// var latLng = new google.maps.LatLng(document.getElementById('lat').value, document.getElementById('long').value);
	var latLng = new google.maps.LatLng(36.45994, -121.89938);

	var mapOptions = {
		center: latLng,
		zoom: 10,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		draggable: false
	}
	var map = new google.maps.Map(mapCanvas, mapOptions);
	
	google.maps.event.addListener(map, "click", function (e){

	    //lat and lng is available in e object
	    var latLng = e.latLng;
	    var marker = new google.maps.Marker({
			position: latLng,
			map: map,
			title: 'Your location'
		});
		// alert( "Latitude: "+ e.latLng.lat()+" "+", longitude: "+ e.latLng.lng() );

		document.getElementById('lat').value = e.latLng.lat();
		document.getElementById('long').value = e.latLng.lng();
	});
}


if (navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(positionFound);
} else {
	alert('It appears that required geolocation is not enabled in your browser.');
}
