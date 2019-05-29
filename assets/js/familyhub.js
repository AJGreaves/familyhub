
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

$('#to-top-btn').click(function() {
    topFunction();
});

$('#search-btn').click(function() {
    openSearch();
});

$('#search-modal-submit-button').click(function() {
    openSearch();
});


// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

// when user clicks on search icon the search modal adds the active class, 
// adding css to display: block; opacity: 1; 
function openSearch() {
    $("#search-modal").toggleClass('active');
}
