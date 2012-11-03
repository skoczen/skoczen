
var formSaveTimeout;
var saveFadeoutTimeout;
var firstSave = true;
$(function(){
	$(".sleep_field input").timeEntry({
		'spinnerImage':'',
		'defaultTime': '10:00AM'
	});
	$(".sleep_field input").each(function(){
		$ele = $(this);
		$ele.focus().blur();
	});
	
	$("input, textarea").live("change",queueFormSave)
	$(".hours input").live("change",hoursChanged)
	$('form').ajaxForm({
		success: saveSuccess,
	});
	$(".hours").each(function(){
		calculateHours($(this));
	});
	$(".shift_left_link").live("click", shiftLeft);
	$(".shift_right_link").live("click", shiftRight);
});

function shiftLeft() {
	$("#right_form").html($("#left_form").html());
	var url = $("#left_form form").attr("prev_day_url");
	setDailyForm(url, $("#left_form"));
	return false;
}
function shiftRight() {
	$("#left_form").html($("#right_form").html());
	var url = $("#right_form form").attr("next_day_url");
	setDailyForm(url, $("#right_form"));
	return false;
}
function setDailyForm(url, target) {
	$.ajax({
		url: url,
		type: "GET",
		dataType: "json",
		success: function(json){
			$(target).html(json.html);
			$('form').ajaxForm({
				success: saveSuccess,
			});
		}
	});
}

function queueFormSave(e) {
	// saving...
	clearTimeout(formSaveTimeout);
	var $ele = $(e.target);
	var $form = $ele.parents("form");
	formSaveTimeout = setTimeout(function(){saveForm($form);}, 1500);
}
function saveForm(form) {
	clearTimeout(formSaveTimeout);
	clearTimeout(saveFadeoutTimeout);
	$("#status").stop().show().html(ich.saving())
	form.submit();
}

function saveSuccess(json) {

	if (json.success) {
		$("#status").html(ich.saved());	
	} else {
		$("#status").html(ich.errored());	
	}
	updateSleepHours();
	
	saveFadeoutTimeout = setTimeout(function(){$("#status").fadeOut();}, 2000);
}

function updateSleepHours() {
	$(".section.hours").each(function(){
		$section = $(this);
		$.ajax({
			url: $section.parents("form").attr("update_url"),
			success: updateSectionWithResponse,
		})
	})
}

function updateSectionWithResponse(json, section) {
	$form = $("#gb_" + json.id);
	$(".sleep .number", $form).html(json.sleep_hrs);
	$(".meditated label", $form).removeClass().addClass("status_label " + json.meditated_status)
	$(".off label", $form).removeClass().addClass("status_label " + json.off_status)
	$(".worked_out label", $form).removeClass().addClass("status_label " + json.worked_out_status)
	$(".left_the_house label", $form).removeClass().addClass("status_label " + json.left_the_house_status)
	$(".nature_time label", $form).removeClass().addClass("status_label " + json.nature_time_status)
}

function hoursChanged(e) {
	$ele = $(e.target);
	$hours = $ele.parents(".hours");
	calculateHours($hours);
}
function roundNumberWithDec(num, dec) {
	return Math.round( Math.round( num * Math.pow( 10, dec + 1 ) ) / Math.pow( 10, 1 ) ) / Math.pow(10,dec);
}
function roundPretty(num) {
	var roundLen = 1;
	var rem = (num % 1) * 100;
	if (rem == 25 || rem == 75) {
		roundLen = 2;
	}
	if (rem == 0) {
		roundLen = 0;
	}
	return roundNumberWithDec(num,roundLen)
}
function calculateHours(hoursBlock) {
	var hours = 0;
	$(".day_hours input", hoursBlock).each(function(){
		hours += parseFloat($(this).val(),10);
	});
	hours = roundPretty(hours);
	var fell_asleep_time = $(".fell_asleep input", hoursBlock).val();
	var woke_up_time =  $(".woke_up input", hoursBlock).val();
	
	fell_asleep_math_time = parseFloat(fell_asleep_time.substr(0,2)) + (parseInt(fell_asleep_time.substr(3,2))/60)
	if (Math.floor(fell_asleep_math_time) == 12) {
		fell_asleep_math_time -= 12;
	}
	if (fell_asleep_time.substr(5,2) == "PM") {
		fell_asleep_math_time += 12;
	}
		

	woke_up_math_time = parseFloat(woke_up_time.substr(0,2)) + (parseInt(woke_up_time.substr(3,2))/60)
	if (Math.floor(woke_up_math_time) == 12) {
		woke_up_math_time -= 12;
	}
	if (woke_up_time.substr(5,2) == "PM") {
		woke_up_math_time += 12;
	}

	if (fell_asleep_math_time < woke_up_math_time) {
		fell_asleep_math_time += 24;	
	}
	

	total_hours_awake = roundPretty(fell_asleep_math_time - woke_up_math_time);
	if (hours == total_hours_awake) {
		$(".total", hoursBlock).html("");	
	} else {
		var diff = total_hours_awake-hours;
		diff =  (diff < 0) ? diff : "+" + diff
		$(".total", hoursBlock).html( diff );	
	}
	
}