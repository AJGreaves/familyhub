/** 
 * checks if page has an element with this id before launching the POST request, 
 * prevents errors in the console on pages that do not contain this element.
 * suggested by fellow student Seán Murphy
 **/

if (document.querySelector('#new-account-form')) {

  const newAccountForm = document.querySelector('#new-account-form');

  newAccountForm.addEventListener('submit', (event) => {
    // prevents default behaviour of submit button to refresh page
    event.preventDefault();

    const username = document.querySelector('#newUsername').value;
    const email = document.querySelector('#newEmailInput').value;
    const password = document.querySelector('#newPasswordInput').value;

    const data = {
      email: email,
      password: password,
      username: username,
    }

    showLoading();

    fetch('/newaccount', {
        method: 'POST',
        cors: '*same-origin',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      })
      .then(res => res.json())
      .then(data => {
        hideLoading();
        if (data.emailExists || data.userExists) {
          userExistsModal(data.emailExists, data.userExists)
        } else {
          confirmAccountModal(username);
        }
      })
      .catch(err => console.log(err));
  });
}

// activation code for modals
$('#closeUserExistsModal').click(function () {
  userExistsModal();
})

/**
 * Constructs welcome message for new account with their username included
 * @param {string} username 
 */

function confirmAccountModal(username) {
  $('#alertHeading').text('Welcome to Family Hub ' + username + '!')
  $('#newUserConfirmModal').addClass('active');
}

/**
 * userExistsModal takes booleans sent from python on if the user or email
 * already exists in the database. Responds with a modal message to give the
 * user the appropriate feedback so they know what to do next.
 * @param {bool} emailExists 
 * @param {bool} userExists 
 */

function userExistsModal(emailExists, userExists) {
  if (emailExists && userExists) {
    $('#alertHeading').text('Hello again');
    $('#alertMessage').text('This account is already registered to Family Hub');
    $('#logInBtn').removeClass('d-none');
  } else if (emailExists) {
    $('#alertHeading').text('Hello again');
    $('#alertMessage').text('This email is already registered to Family Hub');
    $('#logInBtn').removeClass('d-none');
  } else if (userExists) {
    $('#alertHeading').text('Sorry');
    $('#alertMessage').text('This username is already in use, please choose another');
    $('#logInBtn').addClass('d-none');
  }
  $('#userExistsModal').toggleClass('active');
}

/**
 * takes input from the login from and passes it to Flask to check against the database.
 * When the data has been checked and responses return from Flask, the function then 
 * responds to the user in the browser depending on what the response
 */

if (document.querySelector('#login-form')) {

  const loginForm = document.querySelector('#login-form');

  loginForm.addEventListener('submit', (event) => {
    // prevents default behaviour of submit button to refresh page
    event.preventDefault();

    const loginInput = document.querySelector('#loginInput').value;
    const password = document.querySelector('#loginPassword').value;

    const data = {
      loginInput: loginInput,
      password: password
    }
    showLoading();
    fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      })
      .then(res => res.json())
      .then(data => {
        hideLoading();
        if (data.userMatch == false) {
          let message = 'no user match';
          alertModal(message);
        } else if (data.passwordCorrect == false) {
          let message = 'no password match';
          alertModal(message);
        } else if (data.passwordCorrect) {
          openLoggedInModal(data.username);
        }
      })
      .catch(err => console.log(err));

  });
}

/**
 * This function takes a string and constructs the contents 
 * of the alert modal to match the needs for this use.
 * @param {string} message 
 */
function alertModal(message) {
  switch (message) {
    case 'no user match':
      $('#alertHeading').text('Sorry');
      $('#alertMessage').text('No account with this username or email address.\n Please try again.');
      break;
    case 'no password match':
      $('#alertHeading').text('Incorrect password');
      $('#alertMessage').text('Please try again.');
      break;
    case 'times match':
      $('#alertHeading').text('Error');
      $('#alertMessage').text('Your start and finish times cannot be the same.');
      break;
    case 'start end times wrong':
      $('#alertHeading').text('Error');
      $('#alertMessage').text('You selected an earlier finish time than the start time!');
      break;
    default:
      break;
  }
  $('#alertModal').toggleClass('active');
}

$('#alertModalClose').click(function(e) {
  e.preventDefault();
  alertModal();
})

/**
 * Function takes username for this user passed from the 
 * database and constructs a welcome message with it, then
 * activates the modal so it can be seen.
 * @param {string} username 
 */

function openLoggedInModal(username) {
  $('#welcomeMessage').text('Welcome ' + username + '.');
  $('#loggedInModal').addClass('active');
}

/*
 * works with css to slow carousels movement down 
 * Credit: https://stackoverflow.com/questions/17332431/how-can-i-control-the-speed-that-bootstrap-carousel-slides-in-items/18633703 
 */
jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 2000;

// CREDIT: code for floating buttons taken from https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
window.onscroll = function () {
  scrollFunction();
};

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

$('#to-top-btn').click(function () {
  topFunction();
});

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

$('#search-btn').click(function () {
  openSearch();
});

$('#search-modal-submit-button').click(function () {
  openSearch();
});

// when user clicks on search icon the search modal adds the active class, 
// adding css to opacity: 1; 
function openSearch() {
  $("#search-modal").toggleClass('active');
}

$('#delete-button').click(function () {
  openDeleteWarningModal();
});

$('#delete-modal-submit-button').click(function () {
  openDeleteWarningModal();
});

function openDeleteWarningModal() {
  $('#delete-warning-modal').toggleClass('active');
}


// datepicker function code written by fellow student Sean Murphy, 
// who gave it to me to demonstrate how to get it working
['#eventFilterDatepickerSm',
  '#eventFilterDatepickerLg',
  '#start',
  '#end',
  '#date'
].forEach(datepick => {
  $(datepick).datepicker({
    autoclose: true,
    todayHighlight: true,
    uiLibrary: 'bootstrap4',
    format: 'dd/mm/yyyy',
    todayBtn: "linked",
    language: "it",
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
  '#sunEnd',
].forEach(timepick => {
  $(timepick).timepicker({
    autoclose: true,
    uiLibrary: 'bootstrap4'
  });
});


/**
 * Spinner animation. 
 */

function showLoading() {
  document.getElementById("spinner-wrapper").style = "visibility: visible";
}

function hideLoading() {
  document.getElementById("spinner-wrapper").style = "visibility: hidden";
}

/**
 * toggle disabled/required attributes on elements when on/off switch clicked
 */

$('#isFree').click(function () {
  let $from = $('#from');

  if ($from.attr('required')) {
    $from.attr('disabled', '').removeAttr('required');
    $from.val('0');
  } else {
    $from.attr('required', '').removeAttr('disabled');
  }
})

/* to activate fields to input start / end times for days only when that day is clicked */

$(".click-days-js").click(function () { 
  let day = this.id;
  activateTimes($('#' + day + 'Start'), $('#' + day + 'End'), $('.' + day + '-times'));
});


function activateTimes($start, $end, $times) {
  if ($start.attr('required')) {
    $start.attr('disabled', '').removeAttr('required').val('');
    $end.attr('disabled', '').removeAttr('required').val('');
    $times.each(function(){
      $(this).removeClass('active');
    })
  } else {
    $start.attr('required', '').removeAttr('disabled');
    $end.attr('required', '').removeAttr('disabled');
    $times.each(function(){
      $(this).addClass('active');
    })
  }
}

/**
 * activates functions to count and compare opening times
 * on each day of the week
 */
$('input.compare-js').change(function() {
  
  let dayId = this.id;
  let day = dayId.substring(0, 3);

  if (day === 'sta' || day === 'end') {
    if (countTimes("date")) {
      compareDates("date");
    }
  }

  if (countTimes(day)) {
    compareTimes(day);
  }

})

/**
 * Returns true if both start and end fields for a specific
 * day of the week have been filled in
 * @param {string} day 
 */

function countTimes(day) {
  let count = 0;
  let selector = $('.compare-'+ day +'-js');

  selector.each(function(){
    if ($(this).val().length > 0 ) {
      count += 1;
    } 
  });

  if (count == 2) {
    return true;
  } else {
    return false
  }
}

/**
 * Function takes array of two values times and compares them to see if the 
 * user selected end time the same as or before the start time. If incorrect input 
 * the end time is deleted so user cannot submit form with incorrect data
 * @param {string} day 
 */

function compareTimes(day) {
  
  let times = [];
  input =  $('.compare-' + day + '-js');
  dayId = $('#' + day + 'End');

  input.each(function() {
    let time = $(this).val();
    times.push(time);
  })

  first = times[0].split(':').map(Number);
  second = times[1].split(':').map(Number);

  if ((first[0] === second[0]) && (first[1] === second[1])) {
    alertModal("times match");
    dayId.val('');
  } else if ((first[0] > second[0]) || ((first[0] === second[0]) && (first[1] > second[1]))) {
    alertModal("start end times wrong");
    dayId.val('');
  } 
  
}

function compareDates(key) {
  let dates = [];
  input =  $('.compare-' + key + '-js');

  input.each(function() {
    let date = $(this).val();
    dates.push(date);
  })

  first = dates[0].split('/').map(Number);
  second = dates[1].split('/').map(Number);

  if (first[0] === second[0] && first[1] === second[1] && first[2] === second[2]) {
    alert('those dates are the same!');
    $('#end').val('');
  } else if (first[2] > second[2] 
          || first[2] === second[2] && first[1] > second[1]
          || first[2] === second[2] && first[1] === second[1] && first[0] > second[0]) {
    alert('that end date ('+ dates[1] +') is before the start date ('+ dates[0] +')!');
    $('#end').val('');
  }
}

/**
 * Function to make sure at least one checkbox is selected for categories, 
 * age range and indoor/outdoor in add/edit forms
 */

let selectors = ['#timesInput :', '.in-out-js:', '.age-range-js:', '.categories :' ];
$(selectors).each(function(i) {
  let checkboxGroup = $(selectors[i] + 'checkbox[required]');
  checkboxGroup.change(function(){
    if(checkboxGroup.is(':checked')) {
      checkboxGroup.removeAttr('required');
    } else {
      checkboxGroup.attr('required', 'required');
    }
  });
})

$('.submit-js').click(function () {
  let $from = $('#from');

  if (!$from.attr('required')) {
    $from.attr('required', '').removeAttr('disabled');
    $from.val('0');
  }
})