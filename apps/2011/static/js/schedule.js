/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.10.13
*/
$(function(){
	$('td.desc').popover({title: function(){return $(this).text()}, content:function(){
		var avatar = $(this).attr('avatar')
		if (avatar) {
			return '<img src="/static/images/speakers/' + avatar + '" alt="' + $(this).text() + '" />' + $(this).attr('data-content') + '<div style="clear:both; "></div>'
		} else {
			return $(this).attr('data-content')
		}
    }, html:true})
})