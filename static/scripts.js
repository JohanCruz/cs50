// Google Map
var map;
var fu="abc";

// markers for map
var markers = [];

// info window
var info = new google.maps.InfoWindow();

// execute when the DOM is fully loaded
$(function() {

    // styles for map
    // https://developers.google.com/maps/documentation/javascript/styling
    var styles = [

        // hide Google's labels
        {
            featureType: "all",
            elementType: "labels",
            stylers: [
                {visibility: "off"}
            ]
        },

        // hide roads
        {
            featureType: "road",
            elementType: "geometry",
            stylers: [
                {visibility: "off"}
            ]
        }

    ];

    // options for map
    // https://developers.google.com/maps/documentation/javascript/reference#MapOptions
    var options = {
        center: {lat: 37.4236, lng: -122.1619}, // Stanford, California
        disableDefaultUI: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        maxZoom: 14,
        panControl: true,
        styles: styles,
        zoom: 13,
        zoomControl: true
    };

    // get DOM node in which map will be instantiated
    var canvas = $("#map-canvas").get(0);

    // instantiate map
    map = new google.maps.Map(canvas, options);

    // configure UI once Google Map is idle (i.e., loaded)
    google.maps.event.addListenerOnce(map, "idle", configure);

}); 

function article(str)
{
    // get places matching query (asynchronously)
    var parameters = {
        geo: str
    };
    $.getJSON(Flask.url_for("article"), parameters)
    .done(function(data, textStatus, jqXHR) {
     
        // call typeahead's callback with search results (i.e., places)
        asyncResults(data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {

        // log error to browser's console
        console.log(errorThrown.toString());

        // call typeahead's callback with no results
        asyncResults([]);
    });
}

function art(str,marker) {
  var xhttp;    
  if (str == "") {
    document.getElementById("txtHint").innerHTML = "";
    return;
  }
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        window.fu =JSON.parse(this.responseText); 
        
        console.log( window.fu.length);
        var link="";
        var title="";
        var str2="<UL>";
        for (var i = 0; i < window.fu.length; i++)
        {
            link = window.fu[i].link;
            title= window.fu[i].title;
            str2 =  str2+'<LI><a href="'+link+'"target="_blank">'+title+'</a>'
            
        }
        str2 =  str2+"</UL>";
        showInfo(marker, str2);
        
        return; 
    }
  };
  xhttp.open("GET", "/articles?geo="+str, true);
  xhttp.send();
} 


function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
         markers[i].setMap(map);
    }
}


/**
 * Adds marker for place to map.
 */
function addMarker(place)
{ 

    //window.alert(place.admin_name1);
    //console.log(place.admin_name1);
    
    var myLatlng = new google.maps.LatLng(place.latitude,place.longitude);


    var image = {
          url: 'https://maps.google.com/mapfiles/kml/pal2/icon31.png',
          // This marker is 20 pixels wide by 32 pixels high.
          size: new google.maps.Size(32, 72),
          // The origin for this image is (0, 0).
          origin: new google.maps.Point(0, 0),
          // The anchor for this image is the base of the flagpole at (0, 32).
          anchor: new google.maps.Point(0, 32)
        };
        
    var marker = new google.maps.Marker({ position: myLatlng,title:place.admin_name3+" "+place.admin_name2+" "+place.admin_name1+" "+place.postal_code,map:map,  label: place.place_name+", "+ place.admin_name1 , icon: image});
    
    
    //addMarker(markers);
    markers.push(marker);
    marker.setMap(map);
    
    var geo=place.postal_code
    
    
    
    
    
    var infowindow = new google.maps.InfoWindow({
          content: "hola"
        });
        
    marker.addListener('click', function() {
        art(geo,marker);
        
        //infowindow.open(map, marker);
        
        //for (var i = 0; i < articulos.length; i++)
          // {
               //addMarker(data[i]);
        //setTimeout(function() {
          
          //  console.log(fu);
            
        //}, 250);

       
               
           //}
        });
    
    //window.alert(window.markers[0]);
    //console.log(window.markers);
    
    //showInfo(marker,"hu");
    

        

    // TODO
    
}

/**
 * Configures application.
 */
function configure()
{   
    // update UI after map has been dragged
    google.maps.event.addListener(map, "dragend", function() {

        // if info window isn't open
        // http://stackoverflow.com/a/12410385
        if (!info.getMap || !info.getMap())
        {
            update();
        }
    });

    // update UI after zoom level changes
    google.maps.event.addListener(map, "zoom_changed", function() {
        update();
    });

    // configure typeahead
    $("#q").typeahead({
        highlight: false,
        minLength: 1
    },
    {
        display: function(suggestion) { return null; },
        limit: 30,
        

        
        source: search,
        templates: {
            //suggestion: Handlebars.compile( 
            empty: "no places found yet",
            suggestion: Handlebars.compile("<p> {{ place_name }}, {{ admin_name1 }}, {{ postal_code }}</p>")
                    
        }
    });

    // re-center map after place is selected from drop-down
    $("#q").on("typeahead:selected", function(eventObject, suggestion, name) {

        // set map's center
        map.setCenter({lat: parseFloat(suggestion.latitude), lng: parseFloat(suggestion.longitude)});

        // update UI
        update();
    });

    // hide info window when text box has focus
    $("#q").focus(function(eventData) {
        info.close();
    });

    // re-enable ctrl- and right-clicking (and thus Inspect Element) on Google Map
    // https://chrome.google.com/webstore/detail/allow-right-click/hompjdfbfmmmgflfjdlnkohcplmboaeo?hl=en
    document.addEventListener("contextmenu", function(event) {
        event.returnValue = true; 
        event.stopPropagation && event.stopPropagation(); 
        event.cancelBubble && event.cancelBubble();
    }, true);

    // update UI
    update();

    // give focus to text box
    $("#q").focus();
}

/**
 * Removes markers from map.
 */
function removeMarkers()
{   
    setMapOnAll(null);
    window.markers = [];
    // TODO
}

/**
 * Searches database for typeahead's suggestions.
 */
function search(query, syncResults, asyncResults)
{
    // get places matching query (asynchronously)
    var parameters = {
        q: query
    };
    $.getJSON(Flask.url_for("search"), parameters)
    .done(function(data, textStatus, jqXHR) {
     
        // call typeahead's callback with search results (i.e., places)
        asyncResults(data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {

        // log error to browser's console
        console.log(errorThrown.toString());

        // call typeahead's callback with no results
        asyncResults([]);
    });
}

/**
 * Shows info window at marker with content.
 */
function showInfo(marker, content)
{
    // start div
    var div = "<div id='info'>";
    if (typeof(content) == "undefined")
    {
        // http://www.ajaxload.info/
        div += "<img alt='loading' src='/static/ajax-loader.gif'/>";
    }
    else
    {
        div += content;
    }

    // end div
    div += "</div>";

    // set info window's content
    info.setContent(div);

    // open info window (if not already open)
    info.open(map, marker);
}

/**
 * Updates UI's markers.
 */
function update() 
{
    // get map's bounds
    var bounds = map.getBounds();
    var ne = bounds.getNorthEast();
    var sw = bounds.getSouthWest();

    // get places within bounds (asynchronously)
    var parameters = {
        ne: ne.lat() + "," + ne.lng(),
        q: $("#q").val(),
        sw: sw.lat() + "," + sw.lng()
    };
    $.getJSON(Flask.url_for("update"), parameters)
    .done(function(data, textStatus, jqXHR) {

       // remove old markers from map
       removeMarkers();

       // add new markers to map
       for (var i = 0; i < data.length; i++)
       {
           addMarker(data[i]);
       }
    })
    .fail(function(jqXHR, textStatus, errorThrown) {

        // log error to browser's console
        console.log(errorThrown.toString());
    });
};


