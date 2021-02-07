// Creating a readline object
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

// Conditional Example
let x = 10;
let y = 10;
if (x == y) {
	console.log("Var x (" + x + ") Is Equals to var y (" + y + ")");
} else if (x > y) {
	console.log("Var x (" + x + ") Is Larger than var y (" + y + ")");
} else {
	console.log("Var x (" + x + ") Is Smaller than var y (" + y + ")");
}

// Conditional Example 2
x = 10 > 20 ? "Is Bigger" : "Is Lower";
y = 30 > 20 ? (20 < 30 ? "Is Bigger" : "Is Lower") : "Is Equals";
console.log(x);
console.log(y);

// Conditional Example 3
rl.question("Tahun berapakah yang ingin Anda cek? : ", (A) => {
	if (A % 4 == 0) {
		if (A % 100 == 0) {
			if (A % 400 == 0) {
				console.log("Tahun tersebut merupakan tahun kabisat");
			} else {
				console.log("Tahun tersebut bukan tahun kabisat");
			}
		} else {
			console.log("Tahun tersebut merupakan tahun kabisat");
		}
	} else {
		console.log("Tahun tersebut bukan tahun kabisat");
	}
	rl.close();
});
