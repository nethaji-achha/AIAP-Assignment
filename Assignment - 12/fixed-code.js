// Get input from user with null check
let input = prompt("Enter the list elements separated by spaces:");

// Handle null case (user cancelled the prompt)
if (input === null) {
    console.log("Input cancelled by user");
    // You can either exit or provide a default value
    input = ""; // or use a default like "1 2 3 4 5"
}

let arr = input.split(' ').map(Number);

// Get target element
console.log("Array:", arr);
