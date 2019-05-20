$(function () {
    $('[data-toggle="popover"]').popover()
});

$( ".overlay" ).hover(
    function() {
      $(this).parents("#team").css("background-color", "#1ED171");
    }, function() {
      $(this).parents("#team").css("background-color", "#5CD895");
    }
  );