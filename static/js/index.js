/******************************************
 * JS functions for home page only
 ******************************************/

/*
 * works with css to slow carousels movement down 
 * Credit: https://stackoverflow.com/questions/17332431/how-can-i-control-the-speed-that-bootstrap-carousel-slides-in-items/18633703 
 */
jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 2000;

document.addEventListener("DOMContentLoaded", function() {
    let recSlides = $('#recommended-carousel .carousel-item').not(':first');
    recSlides.each(function() {
        $(this).removeClass('active');
    })
    let sportSlides = $('#sports-carousel .carousel-item').not(':first');
    sportSlides.each(function() {
        $(this).removeClass('active');
    })
    let holidaySlides = $('#holiday-carousel .carousel-item').not(':first');
    holidaySlides.each(function() {
        $(this).removeClass('active');
    })
});
