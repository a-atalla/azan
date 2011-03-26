/* An example for gmap reverse geocoder request
   Edited for azan http://bitbucket.org/a_atalla/azan */
// public variables
var map;
var geocoder;
var address;
var place;
var sel_address;
var sel_longitude;
var sel_latitude;
var center;
// timezone
var gmt = 0;
var daylight = 0;

function initialize() {
  map = new GMap2(document.getElementById("map_canvas"));
  map.setCenter(new GLatLng(30.05,31.25), 2);
  map.setUIToDefault();

  GEvent.addListener(map, "click", getAddress);
  geocoder = new GClientGeocoder();

  addKabaIcon();
}

function addKabaIcon() {
  addIcon('../images/kaba.png',21.423333, 39.823333);
}

function getCenter() {
}

function addIcon(icon, lat, lon) {
  var newIcon = new GIcon();
  newIcon.image = icon;
  newIcon.iconSize = new GSize(20, 20);
  newIcon.shadowSize = new GSize(22, 20);
  newIcon.iconAnchor = new GPoint(6, 6);

  var point = new GLatLng(lat,lon);
  var marker = new GMarker( point, { icon: newIcon} ); 
  map.addOverlay(marker);
}

function addKabaCLine(lat, lon) {
  var polyline = new GPolyline([
    new GLatLng(21.423333, 39.823333),
    new GLatLng(lat, lon)
  ], "#0000FF", 5);
  map.addOverlay(polyline);
}

function getAddress(overlay, latlng) {
  if (latlng != null) {
    address = latlng;
    geocoder.getLocations(latlng, showAddress);
  }
}

function showAddress(response) {
  map.clearOverlays();
  if (!response || response.Status.code != 200) {
    alert("Status Code:" + response.Status.code);
  } else {
    place = response.Placemark[0];
    point = new GLatLng(place.Point.coordinates[1],
			place.Point.coordinates[0]);
    marker = new GMarker(point);
    map.addOverlay(marker);
    setSelectedData();
  }
  
}

// showLocation() is called when you click on the Search button
// in the form.  It geocodes the address entered into the form
// and adds a marker to the map at that location.
function showLocation() {
  var address = document.forms[0].q.value;
  geocoder.getLocations(address, showAddress);
}

function setSelectedData() {
  addKabaIcon();
  addKabaCLine(place.Point.coordinates[1], place.Point.coordinates[0]);
  sel_address = place.address;
  sel_longitude = place.Point.coordinates[0];
  sel_latitude = place.Point.coordinates[1];
  //getTimezone(sel_latitude, sel_longitude);
  mapWidget.fill_location_data(); //tel map widget to fetch data
}

function getTimezone(lat, lon) {
  // get gmt, dst and raw offsets from geonames.org
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET","http://ws.geonames.org/timezone?lat="+ lat + "&lng=" + lon,false);
  xmlhttp.send(null);
  var xmlDoc = xmlhttp.responseXML;
  var raw = xmlDoc.getElementsByTagName('rawOffset')[0].childNodes[0].nodeValue;
  var dst = xmlDoc.getElementsByTagName('dstOffset')[0].childNodes[0].nodeValue;
  gmt = xmlDoc.getElementsByTagName('gmtOffset')[0].childNodes[0].nodeValue;
  daylight = Math.abs(parseFloat(dst) - parseFloat(gmt));
}

function getMapAddress() {
  return sel_address;
}

function getMapLongitude() {
  return sel_longitude;
}

function getMapLatitude() {
  return sel_latitude;
}

function getGmt() {
  return gmt;
}

function getDaylight() {
  return daylight;
}
