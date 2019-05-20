$(function () {
  $('[data-toggle="popover"]').popover()
});

$(".overlay").hover(
  function () {
    $(this).parents("#team").css("background-color", "#1ED171");
  },
  function () {
    $(this).parents("#team").css("background-color", "#5CD895");
  }
);

$(function () {
  if ($(window).width() > 768) {
    if ($(window).scrollTop() > $(".navbar-custom").height()) {
      $('.navbar-custom').css("background-color", "#005519");
    } else {
      $('.navbar-custom').css("background-color", "transparent");
    }
  }
});

$(window).bind('scroll', function () {
  if ($(window).width() > 768) {
    if ($(window).scrollTop() > $(".navbar-custom").height()) {
      $('.navbar-custom').css("background-color", "#005519");
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