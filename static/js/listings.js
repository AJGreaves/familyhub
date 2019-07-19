/******************************************
 * JS functions used only on pages 
 * that display listings
 ******************************************/

if (document.querySelector('#social-share-icons')) {
    addShareButtonLinks();
}

/**
 * Adds links to share buttons so user can share the 
 * page they are currently on in facebook, twitter or by email
 */
function addShareButtonLinks() {
    let link = window.location.href;

    $('#sharePageFb').attr('href', 'https://www.facebook.com/sharer/sharer.php?u=' + link);
    $('#sharePageTwitter').attr('href', 'https://twitter.com/home?status=' + link);
    $('#sharePageEmail').attr('href', 'mailto:?&subject=&body=' + link);
}

$(".no-share").click(function () {
    alertModal('no share');
});

$('#closeNotice').click(function () {
    $('.hide').addClass('hidden');
});