$(function(){

	$(".measurement.gauge").each(function(){
		$ele = $(this);
		var colorStart, colorStop;
		var value = parseFloat($ele.attr("value"));
		var roundedValue = Math.round(value);
		colorStart =  '#222';
		colorStop = '#454545';
		
		var opts = {
		  lines: 12, // The number of lines to draw
		  angle: 0.15, // The length of each line
		  lineWidth: 0.44, // The line thickness
		  pointer: {
		    length: 0.9, // The radius of the inner circle
		    strokeWidth: 0.035, // The rotation offset
		    color: '#000000', // Fill color
		  },
		  "colorStart": colorStart,   // Colors
	 	  "colorStop": colorStop,    // just experiment with them
		  strokeColor: '#E0E0E0',   // to see which ones work best for you
		  generateGradient: true
		};


		var target = document.getElementById($ele.attr("linked_canvas")); // your canvas element
		var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
		gauge.maxValue = 10; // set max gauge value
		gauge.animationSpeed = 32; // set animation speed (32 is default value)
		gauge.set(value); // set actual value
	});
	var winWidth = $(window).width();
	var smallGraphWidth = winWidth/7;
	var bigMobileGraphWidth = winWidth/4;
	if ($(window).width()< 800) {
		$(".measurement.gauge.big").each(function(){
			$ele = $(this);
			var ratio = bigMobileGraphWidth/ $ele.width();
			$ele.css({'width': bigMobileGraphWidth});
			var canv_width = $("canvas", $ele).width();
			var canv_height = $("canvas", $ele).height();
			$("canvas", $ele).css({"width": canv_width*ratio, "height": canv_height*ratio});
		});
	}
	
});