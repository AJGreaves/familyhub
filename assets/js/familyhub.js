$( document ).ready(function() {
// CREDIT: code for floating buttons taken from https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("to-top-btn").style.display = "block";
    document.getElementById("search-btn").style.display = "block";
  } else {
    document.getElementById("to-top-btn").style.display = "none";
    document.getElementById("search-btn").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

function openSearch() {
    $("#search-modal").toggleClass('active');
}

})