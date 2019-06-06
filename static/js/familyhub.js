const newAccountForm = document.querySelector('#new-account-form');

newAccountForm.addEventListener('submit', (event) => {
  event.preventDefault();
  
  const email = document.querySelector('#newEmailInput').value;
  const password = document.querySelector('#newPasswordInput').value;
  const businessName = null;
  
  const data = {
    email: email,
    password: password,
    businessName: businessName,
  }
  
  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(data => console.log(JSON.stringify(data)))
  .catch(err => console.log(err));
});


// works with css to slow carousels movement down https://stackoverflow.com/questions/17332431/how-can-i-control-the-speed-that-bootstrap-carousel-slides-in-items/18633703 */
jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 2000;

// CREDIT: code for floating buttons taken from https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
window.onscroll = function() {scrollFunction()};


// makes floating buttons for search and go to top visible once user starts scrolling.
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    $("#to-top-btn").addClass('active');
    $("#search-btn").addClass('active');
  } else {
    $("#to-top-btn").removeClass('active');
    $("#search-btn").removeClass('active');
  }
}

$('#to-top-btn').click(function() {
    topFunction();
});

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

$('#search-btn').click(function() {
    openSearch();
});

$('#search-modal-submit-button').click(function() {
    openSearch();
});

$('#delete-button').click(function() {
  openDeleteWarningModal();
});

$('#delete-modal-submit-button').click(function() {
  openDeleteWarningModal();
});

// when user clicks on search icon the search modal adds the active class, 
// adding css to display: block; opacity: 1; 
function openSearch() {
    $("#search-modal").toggleClass('active');
}

function openDeleteWarningModal() {
    $('#delete-warning-modal').toggleClass('active');
}

// datepicker function code written by fellow student Sean Murphy, 
// who gave it to me to demonstrate how to get it working
['#eventFilterDatepickerSm', 
'#eventFilterDatepickerLg', 
'#start', 
'#end',
'#date'].forEach(datepick => {
    $(datepick).datepicker({ 
    autoclose: true, 
  	todayHighlight: true,
  	uiLibrary: 'bootstrap4'
	});
});

['#monStart', 
'#monEnd',
'#tueStart', 
'#tueEnd',
'#wedStart', 
'#wedEnd',
'#thuStart', 
'#thuEnd',
'#friStart', 
'#friEnd',
'#satStart', 
'#satEnd',
'#sunStart', 
'#sunEnd',].forEach(timepick => {
    $(timepick).timepicker({ 
    autoclose: true, 
  	uiLibrary: 'bootstrap4'
	});
});