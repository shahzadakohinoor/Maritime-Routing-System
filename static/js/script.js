// Maritime Routing System JavaScript

console.log("Maritime Routing System Loaded");

// Welcome Message
window.onload = function () {
    console.log("Application Started");
};

// Route Validation
function validateRouteForm() {

    let source = document.getElementById("source").value;
    let destination = document.getElementById("destination").value;
    let distance = document.getElementById("distance").value;
    let speed = document.getElementById("speed").value;

    if (
        source === "" ||
        destination === "" ||
        distance === "" ||
        speed === ""
    ) {
        alert("Please fill all fields");
        return false;
    }

    if (distance <= 0) {
        alert("Distance must be greater than zero");
        return false;
    }

    if (speed <= 0) {
        alert("Speed must be greater than zero");
        return false;
    }

    return true;
}

// Weather Risk Calculator
function calculateWeatherRisk() {

    let waveHeight = 4.2;

    if (waveHeight >= 4) {
        return "High";
    }

    if (waveHeight >= 2) {
        return "Medium";
    }

    return "Low";
}

// AI Recommendation
function aiRecommendation() {

    let risk = calculateWeatherRisk();

    let recommendation = "";

    if (risk === "High") {

        recommendation =
            "Recommended: 8° Southward Diversion Route";

    } else if (risk === "Medium") {

        recommendation =
            "Proceed with caution and monitor weather";

    } else {

        recommendation =
            "Continue on planned route";
    }

    console.log(recommendation);

    return recommendation;
}

// Fuel Cost Estimation
function calculateFuelCost(days) {

    let fuelPerDay = 32;
    let fuelPrice = 463;

    let fuelUsed = days * fuelPerDay;

    let fuelCost = fuelUsed * fuelPrice;

    return fuelCost.toFixed(2);
}

// Voyage Summary
function showVoyageSummary() {

    let distance = document.getElementById("distance").value;
    let speed = document.getElementById("speed").value;

    if (distance === "" || speed === "") {
        return;
    }

    let days = distance / (speed * 24);

    let fuelCost = calculateFuelCost(days);

    console.log("Voyage Days:", days.toFixed(2));
    console.log("Fuel Cost:", fuelCost);
}

// Auto Update
setInterval(function () {

    let risk = calculateWeatherRisk();

    console.log("Weather Risk:", risk);

}, 30000);

// Dashboard Statistics
function loadDashboard() {

    console.log("Loading Dashboard");

    let voyages = 25;
    let vessels = 8;

    console.log("Voyages:", voyages);
    console.log("Vessels:", vessels);
}

// Initialize
loadDashboard();