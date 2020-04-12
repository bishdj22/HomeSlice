import {Typed} from 'typed.js';

function jumpScroll() {
	window.scroll(0,150); // horizontal and vertical scroll targets
}

var typed = new Typed('#typed',{
	stringsElement: '#typed-strings',
	backSpeed: 40,
	typeSpeed: 40
});