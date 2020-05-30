// Find all iframes
var $iframes = $( "iframe" );
 
// Find &amp;amp;#x26; save the aspect ratio for all iframes
$iframes.each(function () {
  $( this ).data( "ratio", this.height / this.width )
    // Remove the hardcoded width &amp;amp;#x26; height attributes
    .removeAttr( "width" )
    .removeAttr( "height" );
});
 
// Resize the iframes when the window is resized
$( window ).resize( function () {
  $iframes.each( function() {
    // Get the parent container&amp;amp;#x27;s width
    var width = $( this ).parent().width();
    $( this ).width( width )
      .height( width * $( this ).data( "ratio" ) );
  });
// Resize to fix all iframes on page load.
}).resize();


var reload = function(){
  window.location.reload()
}

// Get the element
var elements = document.getElementsByClassName("column");
var grd = document.getElementsByClassName("grid-container");

// Declare a loop variable
var i;
var g;

// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  }
  var curr = document.getElementById("hide");
  var ahead = document.getElementById("show");
  var lst = document.getElementById("list_con");
  var grd = document.getElementById("gri