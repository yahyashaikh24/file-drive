container').removeChild(div_id);
        // location.reload()
      }
    });
  }

  var file_detail = function(){
    var ret = num.split("-");
    var det = document.getElementById('f_details');
    det.innerHTML = '<div><img src="'+thumbnail_img[ret[0]]+'" alt="thumb" width="200px" height="200px"/><br><br>Filename:  '+file_name[ret[0]]+'</div>';
  }

  var items = [
    // { type: 'item', title: ' &nbsp;   Make a Copy', icon: 'fas fa-copy', fn: clicked },
    { type: 'item', title: ' &nbsp;  Download', icon:'fas fa-cloud-download-alt' , fn: download_f },
    { type: 'item', title: ' &nbsp;  Rename', icon: 'fas fa-pen', fn: rename_f },
    { type: 'item', title: ' &nbsp;  Properties', icon: 'fas fa-info-circle', fn: file_detail },
    { type: 'separator' },
    { type: 'item', title: ' &nbsp;  Remove', icon: 'f