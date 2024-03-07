let slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showSlides() {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
  setTimeout(showSlides, 2000);
}

showSlides();
