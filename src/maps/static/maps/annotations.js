// -- Interactive features --


let currentAnnotation = 'marker';
let linePoints = [];
let polyPoints = [];
let markerCount = 0;
const MAX_POINTS = 10;
const SNAP_DISTANCE = 10; // pixels
let annotations = []; // store all annotations
var tempLine = null;
var tempPolyline = null;
var annotationMode = false;

// custom annotations
var mechanicalIcon = "{% static 'maps/icons/gear-complex-solid.svg' %}";
var electricalIcon = "{% static 'maps/icons/plug-solid.svg' %}";
var plumbingIcon = "{% static 'maps/icons/pipe-valve-solid.svg' %}";
var lineIcon = "{% static 'maps/icons/pen-line-regular.svg' %}";
var polygonIcon = "{% static 'maps/icons/draw-polygon-regular.svg' %}";
var markerIcon = "{% static 'maps/icons/location-dot-solid.svg' %}";
var tagIcon = "{% static 'maps/icons/tag-solid.svg' %}";
var stickyNoteIcon = "{% static 'maps/icons/notes-solid.svg' %}";


// func to start annotation placement
function startAnnotation() {
    annotationMode = true;
}

// 
document.getElementById('annotationControls').addEventListener('change', function(e) {
    currentAnnotation = e.target.value;
    linePoints = []; // Reset line points
    polyPoints = []; // Reset polygon points
});


// let the users click on the map to add annotations.
mymap.on('click', function(e) {
    if (currentAnnotation === 'marker') {
        if (markerCount < MAX_POINTS) {
            var newMarker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(mymap);
            var text = promt("Enter text for this marker:", "Marker description");
            if (text != null && text != "" ) {
                newMarker.bindPopup(text).openPopup();
            } else {
                newMarker.bindPopup("Marker at " + e.latlng.toString()).openPopup();
            }
            markerCount++;
            annotations.push(newMarker);
        } else {
            alert("Maximum of 10 markers reached.");
        }
    } else if (currentAnnotation === 'line') {
        if (linePoints.length < MAX_POINTS) {
            linePoints.push([e.latlng.lat, e.latlng.lng]);
    
            // Remove the previous temporary line if it exists
            if (tempLine) {
                mymap.removeLayer(tempLine);
                annotations = annotations.filter(function(annotation) { return annotation !== tempLine; });
            }

            // Create a new temporary line
            tempLine = L.polyline(linePoints, { color: 'red' }).addTo(mymap);
            var lineText = prompt("Enter text for this line:", "Line description");
            if (lineText != null && lineText != "" ) {
                tempLine.bindPopup(lineText);
            } else {
                tempLine.bindPopup("Line at " + e.latlng.toString()).openPopup();
            }
            annotations.push(tempLine); // Add the line to the annotations array
        } else {
            alert("Maximum of 10 points reached for a line.");
        }
    } else if (currentAnnotation === 'polygon') {
        if (polyPoints.length < MAX_POINTS) {
            let point = [e.latlng.lat, e.latlng.lng];
            polyPoints.push(point);

            // Update or create a polyline for the polygon points
            if (polyPoints.length > 1) {
                if (tempPolyline) {
                    mymap.removeLayer(tempPolyline);
                    annotations = annotations.filter(function(annotation) { return annotation !== tempPolyline; });
                }
                tempPolyline = L.polyline(polyPoints, { color: 'green' }).addTo(mymap);
                annotations.push(tempPolyline); // Add the temporary polyline to the annotations array
            }

            // check for snapping
            if (polyPoints.length > 2 && isPointCloseToFirst(polyPoints, point)) {
                var newPolygon = L.polygon([...polyPoints, polyPoints[0]], { color: 'blue' }).addTo(mymap);
                var polyText = prompt("Enter text for this polygon:", "Polygon description");
                if (polyText != null && polyText != "" ) {
                    newPolygon.bindPopup(polyText);
                } else {
                    newPolygon.bindPopup("Polygon at " + e.latlng.toString()).openPopup();
                }
                annotations.push(newPolygon); // Add the completed polygon to the annotations array
                alert("Polygon completed by snapping!");
                saveAnnotation('polygon', [...polyPoints, polyPoints[0]]);
                polyPoints = []; // reset after drawing the polygon
                if (tempPolyline) {
                    mymap.removeLayer(tempPolyline);
                    annotations = annotations.filter(function(annotation) { return annotation !== tempPolyline; });
                    tempPolyline = null;
                } 
            }
        } else {
            alert("Maximum of 10 points reached for a polygon.");
        }
    }
});


function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return false;
}

var latitude = getQueryVariable('lat');
var longitude = getQueryVariable('lng');
var zoomLevel = getQueryVariable('zoom');

if (latitude && longitude && zoomLevel) {
    mymap.setView([parseFloat(latitude), parseFloat(longitude)], parseInt(zoomLevel));
}

document.getElementById('completeLine').addEventListener('click', function() {
    if (linePoints.length > 1) {
        L.polyline(linePoints, { color: 'red' }).addTo(mymap);
        saveAnnotation('line', linePoints);
        linePoints = [];
    } else {
        alert("You need at least 2 points to make a line.");
    }
});

document.getElementById('completePolygon').addEventListener('click', function() {
    if (polyPoints.length > 2) {
        var completedPolygon = L.polygon(polyPoints, { color: 'blue' }).addTo(mymap);
        annotations.push(completedPolygon); // Add the completed polygon to the annotations array
        saveAnnotation('polygon', polyPoints);
        polyPoints = []; // Reset after drawing the polygon
        if (tempPolyline) {
            mymap.removeLayer(tempPolyline);
            annotations = annotations.filter(function(annotation) { return annotation !== tempPolyline; });
            tempPolyline = null;
        }
    } else {
        alert("You need at least 3 points to make a polygon.");
    }
});

document.getElementById('clearAnnotations').addEventListener('click', function() {
    annotations.forEach(function(annotation) {
        mymap.removeLayer(annotation);
    });
    annotations = [];
    linePoints = [];
    polyPoints = [];
    markerCount = 0;
    if (tempLine) {
        mymap.removeLayer(tempLine);
    }
    if (tempPolyline) {
        mymap.removeLayer(tempPolyline);
    }
    tempLine = null;
    tempPolyline = null;
});

function isPointCloseToFirst(points, newPoint) {
    if (points.length > 0) {
        var firstPoint = mymap.latLngToLayerPoint(L.latLng(points[0]));
        var newLayerPoint = mymap.latLngToLayerPoint(L.latLng(newPoint));
        var distance = firstPoint.distanceTo(newLayerPoint);
        return distance <= SNAP_DISTANCE;
    }
    return false;
}    

function saveAnnotation(type, coordinates, metadata) {
    var data = {
        annotation_type: type,
        coordinates: coordinates,
        metadata: metadata
    };
    // AJAX call to Django POST endpoint
    // Handle response and errors
}

// On map load
map.on('load', function() {
    // AJAX call to Django GET endpoint
    // Iterate over the response data and add each annotation to the map
});
