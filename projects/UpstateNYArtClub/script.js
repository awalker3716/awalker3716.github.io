let slideIndex = 0;
showSlides(); // call showslide method

function plusSlides(n){
    showSlides(slideIndex+=n);
}
function currentSlide(n){
    showSlides(slideIndex = n);
    
}

function showSlides() {
	let i;

	// get the array of divs' with classname image-sliderfade
	let slides = document.getElementsByClassName("mySlides");

	// get the array of divs' with classname dot
	let dots = document.getElementsByClassName("dot");

	for (i = 0; i < slides.length; i++) {
		// initially set the display to
		// none for every image.
		slides[i].style.display = "none";
	}

	// increase by 1, Global variable
	slideIndex++;

	// check for boundary
	if (slideIndex > slides.length) {
		slideIndex = 1;
	}

	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(" active", "");
	}

	slides[slideIndex - 1].style.display = "block";
	dots[slideIndex - 1].className += " active";

	// Change image every 2 seconds
	setTimeout(showSlides, 2000);
}
