/******************************************
 * JS functions used on all/most pages
 ******************************************/

// Shows spinner and hides page content until everything is loaded
document.addEventListener("DOMContentLoaded", function() {
    hideLoading();
    $('.no-fouc').removeClass('no-fouc');
    return;
});

// Show and hide spinner animation
function showLoading() {
    document.getElementById("spinner-wrapper").style = "visibility: visible";
    return;
}

function hideLoading() {
    document.getElementById("spinner-wrapper").style = "visibility: hidden";
    return;
}

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

// When the user clicks on the button, scroll to the top of the page
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// when user clicks on search icon the search modal adds the active class, 
// adding css to opacity: 1; 

$('.open-close-search-js').click(function () {
    $("#search-modal").toggleClass('active');
});

// animate changes in icons to reflect collapsed / opened elements on the page
$(".collapse-link").click(function () {
    $(this).children('i').toggleClass('fa-chevron-up').toggleClass('fa-chevron-down');
})

/*----------------------------------------
 * JS Modals
----------------------------------------*/

/**
 * This function takes a string and constructs the contents 
 * of the alert modal to match the needs for this use.
 * @param {string} message 
 */

function alertModal(message, date1, date2) {
    const heading = $('#alertHeading');
    const message1 = $('#alertMessage');
    const message2 = $('#alertMessageLine2');

    switch (message) {
        case 'no user match':
            heading.text('Sorry');
            message1.text('No account with this username or email address.\n Please try again.');
            break;
        case 'no password match':
            heading.text('Incorrect password');
            message1.text('Please try again.');
            break;
        case 'times match':
            heading.text('Error');
            message1.text('Your start and finish times cannot be the same.');
            break;
        case 'start end times wrong':
            heading.text('Error');
            message1.text('You selected an earlier finish time than the start time.');
            break;
        case 'dates match':
            heading.text('Error');
            message1.text('Your start and finish dates cannot be the same.');
            break;
        case 'start end dates wrong':
            heading.text('Error');
            message1.text('You input a finish date ' + date2);
            message2.text('that is before your start date ' + date1);
            break;
        case 'passwords must not match':
            heading.text('Error');
            message1.text('These passwords are the same.');
            break;
        case 'emails must not match':
            heading.text('Error');
            message1.text('These emails are the same.');
            break;
        case 'email updated':
            heading.text('Success');
            message1.text('Your email has been successfully updated.');
            break;
        case 'password updated':
            heading.text('Success');
            message1.text('Your password has been successfully updated.');
            break;
        case 'email incorrect':
            heading.text('Error');
            message1.text('Current email is incorrect.');
            break;
        case 'password incorrect':
            heading.text('Error');
            message1.text('Current password is incorrect.');
            break;
        case 'no share':
            heading.text('Sorry');
            message1.text("You can't share this page in preview mode.");
            message2.text('Once you have published it, the share links will work');
            break;
        default:
            break;
    }
    $('#alertModal').toggleClass('active');
    return;
}

$('#alertModalClose').click(function (event) {
    event.preventDefault();
    alertModal();
    return;
})

$('.delete-button').click(function () {
    let activity_id = this.id;
    let href = '/deletelisting?activity_id=' + activity_id 
    $('#confirm-delete').attr('href', href);
    openDeleteWarningModal();
});

$('#delete-modal-submit-button').click(function () {
    openDeleteWarningModal();
});

function openDeleteWarningModal() {
    $('#delete-warning-modal').toggleClass('active');
}

/**
 * Function takes username for this user passed from the 
 * database and constructs a welcome message with it, then
 * activates the modal so it can be seen.
 * 
 * BUG FIX: this function also uses the username variable to construct the nessasary 
 * urls for the login page modal. As the modal exists on the page before the user is
 * logged in. the usual session user variable could not be used to create these links 
 * @param {string} username 
 */

function openLoggedInModal(username) {
    let name = capFirst(username);
    $("#accountUrl").attr("href", `/account/${username}`)
    $("#newActivityUrl").attr("href", `/editor/${username}/add-new-activity`)
    $('#welcomeMessage').text('Welcome ' + name + '.');
    $('#loggedInModal').addClass('active');
}

/**
 * Function takes a string and capitalizes the first letter.
 * Code credit: https://paulund.co.uk/how-to-capitalize-the-first-letter-of-a-string-in-javascript
 * @param {string} string 
 */

function capFirst(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}