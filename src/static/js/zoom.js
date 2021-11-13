window.onload = function() {
	const myPic = document.getElementById('image');
	const rect = myPic.getBoundingClientRect();
	const zPic = document.getElementById('zoomed-image');
	zPic.style.background = "url('" + myPic.src + "')" + " no-repeat";
	var ree = zPic.getBoundingClientRect();
	zPic.style.backgroundSize = myPic.width*4 + "px " + myPic.height*4 + "px";
	var zoomWidth = ree.right - ree.left;
	zoomHeight = (9*zoomWidth)/16;
	zPic.style.height = zoomWidth + "px";
		
	document.addEventListener('mousemove', e => {
		e.preventDefault();
		x = e.clientX - rect.left;
		x1 = e.clientX - zoomWidth/8 - rect.left;
		y = e.clientY - rect.top;
		y1 = e.clientY - zoomWidth/8 - rect.top;
		zPic.style.backgroundPosition = "-" + (4 * x1) + "px " + "-" + (4*y1) + "px";
	});
};

