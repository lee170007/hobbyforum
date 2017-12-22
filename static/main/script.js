window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 2000);

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}