#!/usr/bin/node
const Square5 = Require('./5-square.js');
class Square extends Square5 {
	charprint (c) {
		if (typeof(c) === 'undefined') {
			c = 'x';
		}
	for (i = 0; i < this.height; i++) {
		console.log(c.repeat(this.width));
	}
	}
}
module.exports = Square;
