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
  var grd = document.getElementById("grid_con");
  curr.style.display = "block";
  ahead.style.display = "none";
  lst.style.display = "block";
  grd.style.display = "none";
  
}

// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "50%";
  }

// document.addEventListener('DOMContentLoaded', function(){
//   chld.addEventListener('contextmenu', grid);
// }
// )
  var curr = document.getElementById("show");
  var ahead = document.getElementById("hide");
  var lst = document.getElementById("list_con");
  var grd = document.getElementById("grid_con");
  curr.style.display = "block";
  ahead.style.display = "none";
  lst.style.display = "none";
  grd.style.display = "block";
}


/* Optional: Add active class to the current button (highlight it) */
var container = document.getElementById("btnContainer");
var btns = container.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

// Right Click menus
var html = function(e) {

  var clicked = function() { alert('Item clicked!') }

  var items = [
    // { type: 'item', title: 'Download', icon: 'ion-plus-round', fn: clicked },
    // { type: 'item', title: 'Reset Login', icon: 'ion-person', fn: clicked },
    // { type: 'item', title: 'Help', icon: 'ion-help-buoy', fn: clicked },
    // { type: 'separator' },
    // { type: 'item', title: 'Logout', icon: 'ion-log-out', fn: clicked }
  ]

  basicContext.show(items, e)

}

// Get file location using first element of div 
var num;

// Get into Grid
var grid = function(e) {
  var clicked = function() { alert('Item clicked!') }
  
  // Download files
  var download_f = function() {
    var ret = num.split("-");
    var down = document.createElement('a');
    down.href = 'media\\'+user_id+'\\'+file_path[ret[0]];
    down.download = 'media\\'+user_id+'\\'+file_path[ret[0]];
    document.querySelector('div.grid-container').appendChild(down);
    down.click();
    
    document.querySelector('div.grid-container').removeChild(down);    
    }

  var rename_f = function(){
    Prompt.render('Rename','rename_file_js');
  }
  var delete_f = function(){
    var ret = num.split("-");
    var test_div = {
      file_location: file_path[ret[0]],
      file_del: file_name[ret[0]],
    };
    $.ajax({
      type: "POST",
      url: file_del,
      data: { csrfmiddlewaretoken: csr, text:test_div },
      success: function callback(response) {
        _res = response;
        var div_id = document.getElementById(num);
        document.querySelector('div.grid-container').removeChild(div_id);
        // location.reload()
      }
    });
  }

  var file_detail = function(){
    var ret = num.split("-");
    var det = document.getElementById('f_details');
    det.innerHTML = '<div><img src="'+thumbnail_img[ret[0]]+'" alt="thumb" class="img-thumbnail" width="200px" height="200px"/><br><br>Filename:  '+file_name[ret[0]]+'</div>';
  }

  var items = [
    // { type: 'item', title: ' &nbsp;   Make a Copy', icon: 'fas fa-copy', fn: clicked },
    { type: 'item', title: ' &nbsp;  Download', icon:'fas fa-cloud-download-alt' , fn: download_f },
    { type: 'item', title: ' &nbsp;  Rename', icon: 'fas fa-pen', fn: rename_f },
    { type: 'item', title: ' &nbsp;  Properties', icon: 'fas fa-info-circle', fn: file_detail },
    { type: 'separator' },
    { type: 'item', title: ' &nbsp;  Remove', icon: 'fas fa-trash', fn: delete_f }
  ]

  basicContext.show(items, e)

}

// this.className
document.addEventListener('DOMContentLoaded', function() {
  for (i = 0; i < elements.length; i++){
    var chld = document.createElement('div');
    chld.id = i+'-a';
    chld.className = i+"-container";
    chld.addEventListener('contextmenu',grid);
    // var name = file_name[i].substr(0,9);
    chld.innerHTML = '<div class="name">'+file_name[i]+'</div><img src="'+thumbnail_img[i]+'" alt="thumb" width="200px" height="200px" /><br>';
    document.querySelector('div.grid-container').appendChild(chld);
    chld.style.boxShadow = "5px 5px 5px 5px rgb(197, 197, 197)";
    chld.style.textAlign = "center";
    chld.style.border = "5px solid rgb(221, 221, 221)";
    // document.querySelector('div.list_con').appendChild(chld);
    // Assign ID of current box to num to get file location
    $(chld).hover(function(){
      num = this.id;
    });
  }
  
  document.querySelector('html').addEventListener('contextmenu', html);

});

var rename_file_js = function (val){
  _val = val
  console.log(_val)
  if (_val != ''){
    var ret = num.split("-");
    rename_funct(ret,_val);
  }
  else{
    alert('Aborted! No file name.');
  }
}

function rename_funct(ret,_val) {
  var test_div = {
    file_location: file_path[ret[0]],
    file_old: file_name[ret[0]],
    file_new: _val,
  };
  // var text = "YAHYA SHAIKH"
  $.ajax({
    type: "POST",
    url: file_url,
    data: { csrfmiddlewaretoken: csr, text: test_div },
    success: function callback(response) {
      _res = response
      rename_suc(_res);
    }
  });
}

var rename_suc = function(_res){
  var div_id = document.getElementById(num);
  var child  = div_id.firstChild;
  res = _res.split(",");
  child.innerHTML = res[0];
  location.reload()
  // Change dialog box tympanus.net/codrops/
}

// When the user scrolls the page, execute myFunction
window.onscroll = function() {
  myFunction()
};

// Get the navbar
var navbar = document.getElementsByClassName("btn_reload");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
var myFunction = function(){
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  }
}

function show_user() {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
  var span = document.getElementsByClassName("close")[0];
  span.onclick = function() {
    modal.style.display = "none";
  }
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";      
    }
  }
}
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".grid-container div").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  // Show modal on page load
  $("#compose").modal('show');

  // Hide modal on button click
  $(".hide-modal").click(function(){
      $("#compose").modal('hide');
  });
});