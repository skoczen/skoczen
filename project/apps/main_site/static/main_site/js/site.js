var CENTER_HEIGHT = 100;
var AUTOSCROLL_TIME_INCREMENT = 10;
var AUTOSCROLL_SCROLL_INCREMENT = 80;
var MIN_SCROLL_SPEED = 2;
var scroll_speed = AUTOSCROLL_SCROLL_INCREMENT;
var scroll_ratio = false;
var current_scroll_position = false;
var autoscrolling = false;
var autoscroll_timeout = false;
var autoscroll_start_timeout = false;
var win_width, win_height;

$(function(){
	size_pages();
	$(window).resize(size_pages);
	// $(window).scroll(update_scroll_ratio);
	size_pages();
	// autoscroll();
	// if (!autoscrolling) {
	update_scroll_ratio();
	$(window).bind("mousemove", mouse_moved);
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

function mouse_moved(e) {
	mouse_offset = (e.pageX-$(document).scrollLeft() - (win_width/2)) / (win_width/2);
	scroll_speed = AUTOSCROLL_SCROLL_INCREMENT * mouse_offset;
	scroll_speed = (Math.abs(scroll_speed) < MIN_SCROLL_SPEED) ? MIN_SCROLL_SPEED : scroll_speed;

}

function size_pages() {
	win_width = $(window).width();
	win_height = $(window).height();
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
			scrollLeft: "+=" + scroll_speed,
		}, AUTOSCROLL_TIME_INCREMENT, "linear");	
		autoscroll_timeout = setTimeout(autoscroll, AUTOSCROLL_TIME_INCREMENT);
	}
	
	
	
	
}