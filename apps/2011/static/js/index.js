/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.10.16
*/
$(function(){
    $("#hero-selector > div").filter(":first").addClass('active').end()
                             .click(function(){
								  $(":animated").stop(true, true)
                                  var current = $("div.active").text()
                                  var clicked = $(this).text()
                                  var offset = (clicked - current) * 880
                                  $(this).addClass("active").siblings().removeClass("active")
                                  $("#content").animate({"left": "-=" + offset + "px"}, "slow")
								  Hero_anim[$(this).attr("id")]()
                              })
	$(".has_sub_schedule").click(function(){
		                       $(this).children('ul').slideDown('slow').end().siblings('.has_sub_schedule').children('ul').slideUp('slow')
		                   })
	$('.speakers img').popover( {title: function(){return $(this).attr('alt')}, placement: 'below' } )
})

$(window).load(function(){
	$("#first").trigger("click")
})

Hero_anim = {
		first: function() {
			$("#first-hero img").css({rotate: "90deg", marginLeft: -50})
			$("#first-hero h1").css({marginRight: -570, opacity: 0})
			$("#first-hero p").css({position: "relative", top: 50, opacity: 0})
			
			var FUNC=[
			function() {$("#first-hero img").animate({rotate: "0deg", marginLeft: 0}, 1000, aniCB);},
			function() {$("#first-hero h1").animate({marginRight: 0, opacity: 1}, 1500, aniCB);},
			function() {$("#first-hero p").animate({top: 0, opacity: 1}, 1500, aniCB);}
			];
			var aniCB=function() {
				$(document).dequeue("Animation");
			}
			$(document).queue("Animation",FUNC);
			aniCB()
	     }
}