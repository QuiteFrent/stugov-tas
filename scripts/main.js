$(function () {
  $('[data-toggle="popover"]').popover()
});

$(function () {
  if ($(window).width() > 768) {
    if ($(window).scrollTop() > $(".navbar-custom").height()) {
      $('.navbar-custom').css("background-color", "#003600");
    } else {
      $('.navbar-custom').css("background-color", "transparent");
    }
  }
});

$(window).bind('scroll', function () {
  if ($(window).width() > 768) {
    if ($(window).scrollTop() > $(".navbar-custom").height()) {
      $('.navbar-custom').css("background-color", "#003600");
    } else {
      $('.navbar-custom').css("background-color", "transparent");
    }
  }
});

var divId;

$('.nav-link').click(function () {
  divId = $(this).attr('href');
  $('html, body').animate({
    scrollTop: $(divId).offset().top - $(".navbar-custom").height()
  }, 100);
});