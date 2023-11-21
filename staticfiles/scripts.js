AOS.init();

// You can also pass an optional settings object
// below listed default settings
AOS.init({
	// Global settings:
	disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
	startEvent: 'DOMContentLoaded', // name of the event dispatched on the document, that AOS should initialize on
	initClassName: 'aos-init', // class applied after initialization
	animatedClassName: 'aos-animate', // class applied on animation
	useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
	disableMutationObserver: false, // disables automatic mutations' detections (advanced)
	debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
	throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)

	// Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
	offset: 120, // offset (in px) from the original trigger point
	delay: 0, // values from 0 to 3000, with step 50ms
	duration: 400, // values from 0 to 3000, with step 50ms
	easing: 'ease', // default easing for AOS animations
	once: false, // whether animation should happen only once - while scrolling down
	mirror: false, // whether elements should animate out while scrolling past them
	anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
});


// color change element start

// Get the element you want to change the background color of
var element = document.getElementById('colorChangeElement');
var colorWrapperElement = document.getElementById('colorWrapper');

// Define the start and end colors
var startColor = '#f2f2f4';
var endColor = '#000014';

// '#99999A'
// Listen to the scroll event
window.addEventListener('scroll', function () {
	// Calculate the scroll progress as a percentage
	var scrollPercentage =
		(window.scrollY - 5000) /
		(document.documentElement.scrollHeight -
			colorWrapperElement.offsetHeight * 5);

	// Calculate the intermediate color
	var intermediateColor = calculateIntermediateColor(
		startColor,
		endColor,
		scrollPercentage
	);

	// Update the background color of the element
	element.style.background = intermediateColor;
});
console.log(window.scrollY)
// Function to calculate the intermediate color based on a percentage
function calculateIntermediateColor(startColor, endColor, percentage) {
	var startRed = parseInt(startColor.substr(1, 2), 16);
	var startGreen = parseInt(startColor.substr(3, 2), 16);
	var startBlue = parseInt(startColor.substr(5, 2), 16);

	var endRed = parseInt(endColor.substr(1, 2), 16);
	var endGreen = parseInt(endColor.substr(3, 2), 16);
	var endBlue = parseInt(endColor.substr(5, 2), 16);

	var intermediateRed = Math.round(startRed + (endRed - startRed) * percentage);
	var intermediateGreen = Math.round(
		startGreen + (endGreen - startGreen) * percentage
	);
	var intermediateBlue = Math.round(
		startBlue + (endBlue - startBlue) * percentage
	);

	var intermediateColor =
		'#' +
		intermediateRed.toString(16).padStart(2, '0') +
		intermediateGreen.toString(16).padStart(2, '0') +
		intermediateBlue.toString(16).padStart(2, '0');

	return intermediateColor;
}

// Select the element to animate
var bigel = document.querySelector('.big-box');

// Create a GSAP timeline
var tl = gsap.timeline();

// Define the animation
tl.fromTo(bigel, { scale: 1 }, { scale: 200 });

// Create a ScrollTrigger
ScrollTrigger.create({
	animation: tl,
	trigger: '.big-logo-section',
	start: ' top 30%',
	end: 'top 80%',
	scrub: true,
	// pin: true,
	onUpdate: function (self) {
			// Get the scroll progress
			var progress = self.progress;

			// Calculate the current scale value
			var scale = 1 + (progress * 100); // Scale from 1 to 60

			// Apply the scale transformation
			gsap.set(bigel, { scale: scale});
	},

	
});


var tlone = gsap.timeline({ paused: true, scrollTrigger: { 
	markers: false,
	trigger: '.stategy-block-img',
	start: 'top 95%',
	end: 'top 70%',
	scrub: true,
} })
.fromTo(".stategy-block-img", { scale: 1 }, { scale: 0.8 });

var tltwo = gsap.timeline({ paused: true, scrollTrigger: {
		markers: false,
		trigger: '.section-grid',
		start: 'top 75%',
		end: 'top 45%',
		scrub: true,
} })
.fromTo(".stategy-block-img",   { scale: 0.8}, { scale: 0.6, x: '30%' });

var tlthree = gsap.timeline({ paused: true, scrollTrigger: { 
		markers: false,
		trigger: '.section-grid',
		start: 'top 46%',
		end: 'top 5%',
		scrub: true,
} })
.fromTo(".stategy-block-img", { scale: 0.6}, { scale: 0.4, y: '50%' });




document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.querySelector(".menu-icon");
  const mobileMenu = document.querySelector(".mobile-menu");

  menuIcon.addEventListener("click", function () {
    mobileMenu.classList.toggle("active");
  });
});
