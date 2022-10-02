// File Upload
let cur=0

function ekUpload(){

    function Init() {
  
      console.log("Upload Initialised");
  
      var fileSelect    = document.getElementById('file-upload'),
          fileDrag      = document.getElementById('file-drag'),
          submitButton  = document.getElementById('submit-button');
  
      fileSelect.addEventListener('change', fileSelectHandler, false);
  
      // Is XHR2 available?
      var xhr = new XMLHttpRequest();
      if (xhr.upload) {
        // File Drop
        fileDrag.addEventListener('dragover', fileDragHover, false);
        fileDrag.addEventListener('dragleave', fileDragHover, false);
        fileDrag.addEventListener('drop', fileSelectHandler, false);
      }
    }
  
    function fileDragHover(e) {
      var fileDrag = document.getElementById('file-drag');
  
      e.stopPropagation();
      e.preventDefault();
  
      fileDrag.className = (e.type === 'dragover' ? 'hover' : 'modal-body file-upload');
    }
  
    function fileSelectHandler(e) {
      // Fetch FileList object
      var files = e.target.files || e.dataTransfer.files;
  
      // Cancel event and hover styling
      fileDragHover(e);

      var table = document.getElementById("uploadtable");

      let msg=''
    
      if(files.length!=0)
        $("#uploadtable tr").remove(); 

      for (var i = 0, f; f = files[i]; i++) {  
        let row = table.insertRow(i);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);

        cell1.innerHTML = '<img src="static/plugins/file.png" height="15rem" width="15rem" alt="#"> File '+(i+1)
        cell2.innerHTML = encodeURI(f.name)

      }

      // Process all File objects
      for (var i = 0, f; f = files[i]; i++) {
        parseFile(f);
        uploadFile(f);
      }
    }
  
    function parseFile(file) {
  
      console.log(file.name);
      
      var imageName = file.name;
  
      var isGood = (/\.(?=ent|pdb|xlsx|csv|xls)/gi).test(imageName);
      if (isGood) {
        document.getElementById('start').classList.add("hidden");
        document.getElementById('response').classList.remove("hidden");
        document.getElementById('notimage').classList.add("hidden");
        // Thumbnail Preview
        document.getElementById('file-image').classList.remove("hidden");
        document.getElementById('file-image').src = URL.createObjectURL(file);
      }
      else {
        document.getElementById('file-image').classList.add("hidden");
        document.getElementById('notimage').classList.remove("hidden");
        document.getElementById('start').classList.remove("hidden");
        document.getElementById('response').classList.add("hidden");
        document.getElementById("file-upload-form").reset();
      }
    }
    
    // Check for the various File API support.
    if (window.File && window.FileList && window.FileReader) {
      Init();
    } else {
      document.getElementById('file-drag').style.display = 'none';
    }
  }

// Update Progress Bar on basis of previous and current progress value
function update(previous,current) {
    var element = document.getElementById("progress-bar");   
    var width = previous;
    var identity = setInterval(scene, 10);
    function scene() {
    if (width >= current) {
        clearInterval(identity);
    } else {
        width++; 
        element.style.width = width + '%'; 
        }
    }
}

function fetchdata(){

  $.ajax({
    url: '/progress',
    type: 'POST',
    success: function(response){
      const obj = JSON.parse(response);
      update(cur,obj['percent'])
      cur=obj['percent']

      $('#progress-msg').text(obj['msg']);
      $('#progress-value').text(obj['percent']+'%')
    },
    error: function(error){
      window.location="/";
      update(0,0)
      $('#progress-msg').text('Waiting for Input..');
      $('#progress-value').text('0%')
    }
  });
}

$(document).ready(function(){
  setInterval(fetchdata,5000);
});

ekUpload();
  