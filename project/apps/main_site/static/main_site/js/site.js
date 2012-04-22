var CENTER_HEIGHT = 100;
var AUTOSCROLL_TIME_INCREMENT = 10;
var AUTOSCROLL_SCROLL_INCREMENT = 80;
var AUTOSCROLL_RESTART_TIME = 100;
var MIN_SCROLL_SPEED = 2;
var scroll_speed = MIN_SCROLL_SPEED;
var scroll_ratio = false;
var autoscrolling = false;
var autoscroll_timeout = false;
var autoscroll_start_timeout = false;
var ignore_mousemove = false;
var win_width, win_height;

$(function(){
	size_pages();
	$(window).resize(size_pages);
	$(window).bind("mousemove", mouse_moved);
	$(window).bind("touchstart", touch_started);
	$(window).bind("touchend", touch_ended);
	if (Modernizr.touch) {
		touch_ui_init();
		$("a").bind("touchstart", open_link);
	}
	size_pages();
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
	autoscroll_start_timeout = setTimeout(start_autoscroll,500);
}

function mouse_moved(e) {
	if (!ignore_mousemove) {
		mouse_offset = (e.pageX-$(document).scrollLeft() - (win_width/2)) / (win_width/2);
		scroll_speed = AUTOSCROLL_SCROLL_INCREMENT * mouse_offset;
		scroll_speed = (Math.abs(scroll_speed) < MIN_SCROLL_SPEED) ? MIN_SCROLL_SPEED : scroll_speed;	
	}
}

function touch_ui_init() {
	AUTOSCROLL_TIME_INCREMENT = 100;
	ignore_mousemove = true;
	$(window).unbind("mousemove");
	scroll_speed = MIN_SCROLL_SPEED * 4;
	$("page .middle_link .middle_hover").css({"display": "block"});
	// CENTER_HEIGHT = 50;
}
function touch_started() {
	$("body").stop();
	autoscrolling = false;
	clearTimeout(autoscroll_timeout);
	// return false;
}
function touch_ended() {
	autoscrolling = true;
	autoscroll_timeout = setTimeout(autoscroll, AUTOSCROLL_RESTART_TIME);
	// return false;
}

function size_pages() {
	win_width = $(window).width();
	win_height = $(window).height();
	$("page").css("width", win_width + "px").css("height", win_height + "px");
	$("pages").css("width", $("page").length * win_width);
	// if (Modernizr.touch) {
	// 	$("page top, page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", (win_height - CENTER_HEIGHT)/8);
	// } else {
		$("page top, page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", (win_height - CENTER_HEIGHT)/5);
	// }
	

	$("page.first").css("width", win_width-55 + "px");
	// $("page.first right_arrow").css("top", (win_height - CENTER_HEIGHT) /2);
	$("page center_bar middle").css("width", win_width - 200 + "px");
	$("pages").css("margin-top", "0px");

	$("body").scrollLeft( scroll_ratio * $(document).width() ) ;
}


function start_autoscroll() {
	clearTimeout(autoscroll_timeout);
	autoscrolling = true;
	autoscroll();
}

function autoscroll() {
	clearTimeout(autoscroll_timeout);
	if (autoscrolling) {
		// console.log(scroll_speed)
		$("body").stop().animate({
			scrollLeft: $("body").scrollLeft() + scroll_speed,
		}, AUTOSCROLL_TIME_INCREMENT, "linear");	
		autoscroll_timeout = setTimeout(autoscroll, AUTOSCROLL_TIME_INCREMENT);
	}
	
	
	
	
}