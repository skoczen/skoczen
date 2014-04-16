$(function(){
    var was_at_top = false;
    $(document).scrollTop(60);
    $(document).scroll(function(){
        if ($(document).scrollTop() <= 0) {
            if (!was_at_top) {
                was_at_top = true;
                $(".nav").addClass("page_top");
            }
        } else {
            if (was_at_top) {
                was_at_top = false;
                $(".nav").removeClass("page_top");
            }
        }
    });
});
