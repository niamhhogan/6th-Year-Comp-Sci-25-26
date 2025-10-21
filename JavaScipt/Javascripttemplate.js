// template-script.js
// Student Template JavaScript File - Add your own functions here!

// TEMPLATE VARIABLES - Replace these with your own
let yourName = "Your Name Here";
let yourSubjects = ["Subject 1", "Subject 2", "Subject 3", "Add More"];
let currentYear = 2025;

// EXAMPLE FUNCTIONS - Customize these for your project

// 1. Welcome message function
function welcomeMessage() {
    alert("Welcome to " + yourName + "'s website! 🎉");
}

// 2. Example function - Replace with your own
function exampleFunction() {
    let userInput = prompt("Enter something interesting:");
    if (userInput) {
        alert("You entered: " + userInput);
    }
}

// 3. Another example function - Replace with your own
function anotherFunction() {
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    alert("Your random number is: " + randomNumber);
}

// 4. YOUR CUSTOM FUNCTIONS - Add your own functions below

function yourFunction1() {
    // Replace this with your own function
    alert("This is your first custom function!");
    // Add your code here
}

function yourFunction2() {
    // Replace this with your own function
    let result = confirm("Do you like learning JavaScript?");
    if (result) {
        alert("Great! Keep learning!");
    } else {
        alert("Don't worry, it gets easier with practice!");
    }
}

function yourFunction3() {
    // Replace this with your own function
    updateInfoDisplay("You clicked your custom button!");
}

// 5. UTILITY FUNCTIONS - You can customize these

function updateInfoDisplay(message) {
    let displayElement = document.getElementById("info-display");
    if (displayElement) {
        displayElement.innerHTML = message;
    }
}

function updateDynamicList() {
    let listElement = document.getElementById("dynamic-list");
    if (listElement) {
        listElement.innerHTML = "";
        yourSubjects.forEach(function(subject, index) {
            let listItem = document.createElement("li");
            listItem.textContent = (index + 1) + ". " + subject;
            listElement.appendChild(listItem);
        });
    }
}

function addToYourList() {
    let newItem = prompt("Add something to your list:");
    if (newItem && newItem.trim() !== "") {
        yourSubjects.push(newItem.trim());
        updateDynamicList();
        alert("Added '" + newItem + "' to your list!");
    }
}

// 6. DARK MODE FUNCTION - Already working, you can customize colors
function toggleDarkMode() {
    let body = document.body;
    let sections = document.querySelectorAll('.section');
    let header = document.querySelector('header');
    let footer = document.querySelector('footer');
    
    if (body.classList.contains('dark-mode')) {
        // Switch back to light mode
        body.classList.remove('dark-mode');
        body.style.backgroundColor = "#f5f5f5";  // Change to your light background color
        body.style.color = "#333";
        
        sections.forEach(function(section) {
            section.style.backgroundColor = "white";  // Change to your light section color
            section.style.color = "#333";
        });
        
        header.style.color = "white";
        footer.style.color = "white";
        
        // Reset all text elements
        let headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        headings.forEach(function(heading) {
            heading.style.color = "";
        });
        
        let paragraphs = document.querySelectorAll('p');
        paragraphs.forEach(function(p) {
            p.style.color = "";
        });
        
        let listItems = document.querySelectorAll('li');
        listItems.forEach(function(li) {
            li.style.color = "";
        });
        
    } else {
        // Switch to dark mode
        body.classList.add('dark-mode');
        body.style.backgroundColor = "#222";  // Change to your dark background color
        body.style.color = "#f5f5f5";
        
        sections.forEach(function(section) {
            section.style.backgroundColor = "#333";  // Change to your dark section color
            section.style.color = "#f5f5f5";
        });
        
        header.style.color = "white";
        footer.style.color = "white";
        
        // Make all text visible in dark mode
        let headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        headings.forEach(function(heading) {
            heading.style.color = "#f5f5f5";
        });
        
        let paragraphs = document.querySelectorAll('p');
        paragraphs.forEach(function(p) {
            p.style.color = "#f5f5f5";
        });
        
        let listItems = document.querySelectorAll('li');
        listItems.forEach(function(li) {
            li.style.color = "#f5f5f5";
        });
    }
}

// 7. INITIALIZATION FUNCTION - Runs when page loads
function initializePage() {
    console.log("Welcome to " + yourName + "'s website!");
    console.log("Page loaded successfully!");
    
    // Update the dynamic list
    updateDynamicList();
    
    // Update info display
    updateInfoDisplay("Page loaded at: " + new Date().toLocaleString());
    
    // You can add more initialization code here
}

// 8. ADD YOUR OWN FUNCTIONS BELOW THIS LINE

/*
Example function template:

function yourFunctionName() {
    // Your code here
    let userInput = prompt("Ask user something:");
    
    if (userInput) {
        // Do something with the input
        alert("Response: " + userInput);
    }
}

// Math function example:
function calculateSomething() {
    let num1 = parseFloat(prompt("Enter first number:"));
    let num2 = parseFloat(prompt("Enter second number:"));
    
    if (!isNaN(num1) && !isNaN(num2)) {
        let result = num1 + num2;  // Change this calculation
        alert("Result: " + result);
    } else {
        alert("Please enter valid numbers!");
    }
}

// Array function example:
function workWithArrays() {
    let newArray = ["item1", "item2", "item3"];
    
    // Do something with the array
    alert("Array contents: " + newArray.join(", "));
}

*/

// RUN INITIALIZATION WHEN PAGE LOADS
document.addEventListener("DOMContentLoaded", initializePage);
