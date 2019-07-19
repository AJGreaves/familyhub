/******************************************
 * JS functions used on all/most pages
 ******************************************/

/**
 * Shows spinner and hides page content until everything is loaded
*/ 
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        hideLoading();
        $('.no-fouc').removeClass('no-fouc');
    }, 2000);
    return;
});

/**
 * Show spinner animation
 */
function showLoading() {
    $("#spinner-wrapper").css("visibility", "visible");
    return;
}

/**
 * Hide spinner animation
 */
function hideLoading() {
    $("#spinner-wrapper").css("visibility", "hidden");
    return;
}

/**
 * CREDIT: code for floating buttons taken from 
 * https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
 */
window.onscroll = function () {
    scrollFunction();
};


/**
 * makes floating button for go to top visible once user starts scrolling.
 */
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $("#to-top-btn").addClass('active');
    } else {
        $("#to-top-btn").removeClass('active');
    }
}

$('#to-top-btn').click(function () {
    topFunction();
});

/**
 * Scrolls the user bACK to the top of the page
 */
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

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
        case 'error':
            heading.text('Error');
            message1.text('Something went wrong. Please try again.');
            break;
        case 'email sent':
            heading.text('Email sent!');
            message1.text('Your email has been sent successfully!');
            message2.text('We will be in touch within 48 hours');
            break;
        case 'business email sent':
            heading.text('Email sent!');
            message1.text('Your email has been sent successfully!');
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
});

/**
 * Inserts the correct urls into the confirm delete modal buttons when one 
 * of the delete buttons on the page are clicked.
 */
$('.delete-button').click(function () {
    let activity_id = this.id;
    let href = '/deletelisting?activity_id=' + activity_id;
    $('#confirm-delete').attr('href', href);
    openDeleteWarningModal();
    return;
});

$('#delete-modal-submit-button').click(function () {
    openDeleteWarningModal();
    return;
});

/**
 * opens the delete warning modal.
 */
function openDeleteWarningModal() {
    $('#delete-warning-modal').toggleClass('active');
    return;
}

/**
 * Function takes username for this user passed from the 
 * database and constructs a welcome message with it, then
 * activates the modal so it can be seen. 
 * @param {string} username 
 */
function openLoggedInModal(username) {
    let name = capFirst(username);
    let slug = slugify(username);
    $("#accountUrl").attr("href", `/account/${slug}`);
    $("#newActivityUrl").attr("href", `/editor/${slug}/add-new`);
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

/**
 * Makes sure that the confirm delete button is only clickable when the user has
 * filled in the correct conformation input.
 */
$('input#inputDELETE').change(function () {
    let val = $('#inputDELETE').val();
    if (val == "DELETE") {
        $('#confirm-delete').removeClass('no-click');
    } else {
        $('#confirm-delete').addClass('no-click');
    }
    return;
});

/**
 * Turns strings into slug friendly ones. Removes special characters, spaces etc, adds -
 * where needed. 
 * Credit: https://medium.com/@mhagemann/the-ultimate-way-to-slugify-a-url-string-in-javascript-b8e4a0d849e1
 * @param {string} string 
 */

function slugify(string) {
    const a = 'àáäâãåăæąçćčđèéėëêęǵḧìíïîįłḿǹńňñòóöôœøṕŕřßśšșťțùúüûǘůűūųẃẍÿýźžż·/_,:;';
    const b = 'aaaaaaaaacccdeeeeeeghiiiiilmnnnnooooooprrssssttuuuuuuuuuwxyyzzz------';
    const p = new RegExp(a.split('').join('|'), 'g');

    return string.toString().toLowerCase()
        .replace(/\s+/g, '-') // Replace spaces with -
        .replace(p, c => b.charAt(a.indexOf(c))) // Replace special characters
        .replace(/&/g, '-and-') // Replace & with 'and'
        .replace(/[^\w\-]+/g, '') // Remove all non-word characters
        .replace(/\-\-+/g, '-') // Replace multiple - with single -
        .replace(/^-+/, '') // Trim - from start of text
        .replace(/-+$/, ''); // Trim - from end of text
}

/**
 * Activates tooltips
 */
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
