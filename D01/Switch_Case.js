// Creating a readline object
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

// Example of a Todolist

// Switch Block
rl.question("Give me a Day! ", (day) => {
	rl.close();
});

let day = "Monday";
let todolist = "";
switch (day) {
	case "Sunday":
		todolist = `Buy Groceries.`;
		break;
	case "Monday":
		todolist = `Free`;
		break;
	case "Tuesday":
		todolist = `Do Homeworks\nClean your room`;
		break;
	case "Wednesday":
		todolist = `Go to the movie theather\nCall your Doctor`;
		break;
	case "Thursday":
		todolist = `Kill someone for fun`;
		break;
	case "Friday":
		todolist = `Free`;
		break;
	case "Saturday":
		todolist = `Help the poor\nRevolutionize the Working Class`;
		break;
	default:
		console.log("Hari yang dimasukkan salah!");
}
console.log(todolist);

let day = "Monday";
let todolist = "";
if (day == "Sunday") {
	todolist = `Buy Groceries.`;
} else if (day == "Monday") {
	todolist = `Free`;
} else if (day == "Tuesday") {
	todolist = `Do Homeworks\nClean your room`;
} else if (day == "Wednesday") {
	todolist = `Go to the movie theather\nCall your Doctor`;
} else if (day == "Thursday") {
	todolist = `Kill someone for fun`;
} else if (day == "Friday") {
	todolist = `Free`;
} else if (day == "Saturday") {
	todolist = `Help the poor\nRevolutionize the Working Class `;
} else {
	console.log("Hari yang dimasukkan salah!");
}
console.log(todolist);
