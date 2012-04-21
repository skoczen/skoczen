var CENTER_HEIGHT = 100;
var AUTOSCROLL_TIME_INCREMENT = 10;
var AUTOSCROLL_SCROLL_INCREMENT = 1.5;
var scroll_ratio = false;
var current_scroll_position = false;
var autoscrolling = false;
var autoscroll_timeout = false;
var autoscroll_start_timeout = false;

$(function(){
	size_pages();
	$(window).resize(size_pages);
	// $(window).scroll(update_scroll_ratio);
	size_pages();
	// autoscroll();
	// if (!autoscrolling) {
	update_scroll_ratio();
	// }
});

function update_scroll_ratio() {
	if (autoscrolling) {
		$("body").stop();
		autoscrolling = false;
	}
	// autoscrolling = false;

	clearTimeout(autoscroll_timeout);
	clearTimeout(autoscroll_start_timeout);
	scroll_ratio = $(document).scrollLeft() / $(document).width();
	current_scroll_position = $(document).scrollLeft();
	autoscroll_start_timeout = setTimeout(start_autoscroll,500);
	
}

function size_pages() {
	var win_width = $(window).width();
	var win_height = $(window).height();
	$("page").css("width", win_width + "px").css("height", win_height + "px");
	$("pages").css("width", $("page").length * win_width);
	$("page top, page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", (win_height - CENTER_HEIGHT)/5);
	$("page.first").css("width", win_width-55 + "px");
	// $("page.first right_arrow").css("top", (win_height - CENTER_HEIGHT) /2);
	$("page center_bar middle").css("width", win_width - 200 + "px");
	$("pages").css("margin-top", "0px");

	$(document).scrollLeft( scroll_ratio * $(document).width() ) ;
}


function start_autoscroll() {
	clearTimeout(autoscroll_timeout);
	autoscrolling = true;
	autoscroll();
}

function autoscroll() {
	clearTimeout(autoscroll_timeout);
	if (autoscrolling) {
		$("body").stop().animate({
			scrollLeft: "+=" + AUTOSCROLL_SCROLL_INCREMENT,
		}, AUTOSCROLL_TIME_INCREMENT, "linear");	
		autoscroll_timeout = setTimeout(autoscroll, AUTOSCROLL_TIME_INCREMENT);
	}
	
	
	
	
}