/******************************************
 * JS functions for home page only
 ******************************************/

/*
 * works with css to slow carousels movement down 
 * Credit: https://stackoverflow.com/questions/17332431/how-can-i-control-the-speed-that-bootstrap-carousel-slides-in-items/18633703 
 */
jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 2000;

document.addEventListener("DOMContentLoaded", function() {
    let slides = $('.carousel-item').not(':first');
    slides.each(function() {
        $(this).removeClass('active');
    })
});