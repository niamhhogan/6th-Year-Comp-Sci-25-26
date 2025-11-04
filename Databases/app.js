// =============================================================================
// FIREBASE SETUP
// =============================================================================

// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.4.0/firebase-app.js";
import { getDatabase, ref, push, onValue } from "https://www.gstatic.com/firebasejs/12.4.0/firebase-database.js";

// ⭐ STUDENTS: Replace this with YOUR Firebase configuration
// Get this from Firebase Console > Project Settings > Your Apps > Web App
const firebaseConfig = {
    apiKey: "YOUR_API_KEY_HERE",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT_ID.firebasedatabase.app",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Variable to store the chart
let myChart;

// =============================================================================
// FUNCTIONS
// =============================================================================

// Function to save data to Firebase
function saveData() {
    // Get the input value
    let userInput = document.getElementById('userInput').value;
    
    // Get current timestamp
    let timestamp = new Date().toLocaleString();
    
    // ⭐ STUDENTS: Change 'myData' to describe your data (e.g., 'studyHours', 'temperature', 'steps')
    let dataRef = ref(database, 'myData');
    
    // Save to Firebase
    push(dataRef, {
        value: userInput,
        time: timestamp
    });
    
    // Clear the input field
    document.getElementById('userInput').value = '';
}

// Function to create the chart
function createChart() {
    let ctx = document.getElementById('dataChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'line', // ⭐ STUDENTS: Change chart type (line, bar, pie, doughnut, etc.)
        data: {
            labels: [],
            datasets: [{
                label: 'My Data', // ⭐ STUDENTS: Change this label (e.g., 'Hours Studied', 'Temperature (°C)')
                data: [],
                borderColor: '#4CAF50',
                backgroundColor: 'rgba(76, 175, 80, 0.1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to update chart with data
function updateChart(dataArray) {
    if (!myChart) return;
    
    // Get last 10 data points
    let recentData = dataArray.slice(0, 10).reverse();
    
    myChart.data.labels = recentData.map(item => item.time);
    myChart.data.datasets[0].data = recentData.map(item => item.value);
    myChart.update();
}

// Function to display data from Firebase
function displayData() {
    // ⭐ STUDENTS: Change 'myData' to match what you used above (must be the same!)
    let dataRef = ref(database, 'myData');
    
    // Listen for data changes in real-time
    onValue(dataRef, (snapshot) => {
        let dataList = document.getElementById('dataList');
        dataList.innerHTML = ''; // Clear the list
        
        let data = snapshot.val();
        if (data) {
            // Convert data to array
            let dataArray = Object.entries(data).map(([key, value]) => value).reverse();
            
            // Update chart
            updateChart(dataArray);
            
            // Display each item in the list
            dataArray.forEach(item => {
                let li = document.createElement('li');
                // ⭐ STUDENTS: Customize how data is displayed (e.g., 'Hours: ${item.value}')
                li.textContent = `Value: ${item.value} - Time: ${item.time}`;
                dataList.appendChild(li);
            });
        } else {
            dataList.innerHTML = '<li>No data yet</li>';
        }
    });
}

// =============================================================================
// INITIALIZE - This runs when the page loads
// =============================================================================

window.addEventListener('DOMContentLoaded', () => {
    // Create the chart
    createChart();
    
    // Add click event to button
    document.getElementById('submitBtn').addEventListener('click', saveData);
    
    // Start listening for data
    displayData();
});
