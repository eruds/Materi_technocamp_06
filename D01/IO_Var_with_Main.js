function Main() {
	// Hello World Example
	console.log("Hello World");

	// Creating a readline object
	const readline = require("readline");
	const rl = readline.createInterface({
		input: process.stdin,
		output: process.stdout,
	});

	// Prompting an Input
	rl.question("What is your name? : ", (name) => {
		console.log(`Hey there ${name}!`);
		rl.close();
	});

	// Variable Declaration
	let x = 10;
	let y = 20;

	// Console log examples
	console.log(x + y);
	console.log("Hello" + "World");

	// Perbandingan
	console.log(1 == 1);
	console.log(x >= y);
}

Main();
