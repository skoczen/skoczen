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
	$(window).resize(size_pages);
	$(window).bind("mousemove", mouse_moved);
	$(window).bind("touchstart", touch_started);
	$(window).bind("touchend", touch_ended);
	if (Modernizr.touch) {
		touch_ui_init();
		// $("a").bind("touchstart", open_link);
	}
	size_pages();
	update_scroll_ratio();
	window.addEventListener("orientationchange", size_pages);
	// setTimeout(size_pages, 2000);
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
	var is_ios = false;
	if (iOS_getViewportSize !== undefined) {
		win_height = iOS_getViewportSize().height;
		$("html, body").css({"height": win_height});
		is_ios = true;
	} else {
		win_height = $(window).height();	
	}
	
	$("page").css("width", win_width + "px").css("height", win_height + "px");
	// alert(win_height);

	if (win_width < 600) {
		CENTER_HEIGHT = 50;
		$("page.first").css("width", win_width+105 + "px");
		$("page center_bar left").css({"background-position": "-30px center"});
		$("page top, page.first").css("height", ((win_height - CENTER_HEIGHT) /2) - CENTER_HEIGHT).css("padding-top", (win_height - CENTER_HEIGHT*1.5)/3);
		$("page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", CENTER_HEIGHT/8);
		$("pages").css("width", ($("page").length * win_width) + 110).css("height", win_height + "px");
		// $("page.first").css({"padding-top": (win_height - CENTER_HEIGHT*4)/20});
		
		if (is_ios) {
			var padding_top = (win_height - CENTER_HEIGHT*1.5)/6;
			$("page top").css({"height": ((win_height - CENTER_HEIGHT) /2) - CENTER_HEIGHT, "padding-top": padding_top});
			$("page.first").css({"height": win_height - padding_top, "padding-top": 0});
			$("page intro").css({"top": padding_top+10});
		}
		// var first_padding = (win_height - CENTER_HEIGHT)/3.75
		// $("page.first").css({"padding-top": first_padding, "height": win_height - first_padding});
	} else {
		$("page top, page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", (win_height - CENTER_HEIGHT)/5);
		$("page.first").css("width", win_width-55 + "px");
		$("pages").css("width", $("page").length * win_width).css("height", win_height + "px");
	}
	
	// if (Modernizr.touch) {
	// 	$("page top, page bottom").css("height", ((win_height - CENTER_HEIGHT) /2) - (win_height - CENTER_HEIGHT)/5).css("padding-top", (win_height - CENTER_HEIGHT)/8);
	// } else {
		
	// }
	

	
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
		$("body").stop().animate({
			scrollLeft: $("body").scrollLeft() + scroll_speed,
		}, AUTOSCROLL_TIME_INCREMENT, "linear");	
		autoscroll_timeout = setTimeout(autoscroll, AUTOSCROLL_TIME_INCREMENT);
	}
	
	
	
	
}