// CS257 end-to-end assignment
// written by Yiming Xia
// 11.9.2022

window.onload = initialize;

function initialize() {
    var fuelbutton = document.getElementById("fuel_consumption");
    fuelbutton.onclick = showFuelCars;
    var co2button = document.getElementById("co2_emission");
    co2button.onclick = showCo2Cars;
    var co2button = document.getElementById("engine_size");
    co2button.onclick = showEngineCars;
}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function showFuelCars() {
    let url = getAPIBaseURL() + '/fuel_consumption/';

    // Send the request to the books API / endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(cars) {
        // Add the <option> elements to the <select> element
        carlist = '';
        for (var k = 0; k<cars.length; k++) {
            var car = cars[k];
            carlist += '<a href="/api/hello/' +  car.linksID + '">' + car.model + ", " + car.make + ", " + car.fuel_consumption + '</a>' + '<br>';
        }
        // change car.make to linksID, change query to include linksID, 
        // in app.route/hello/<linksID> go to database to get data to render template
        var car_fuel_list = document.getElementById("car_list")
        car_fuel_list.innerHTML = carlist;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}


function showCo2Cars() {
    let url = getAPIBaseURL() + '/co2_emission/';

    // Send the request to the books API / endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(cars) {
        // Add the <option> elements to the <select> element
        carlist = '';
        for (var k = 0; k<cars.length; k++) {
            var car = cars[k];
            carlist += '<a href="/api/hello/' +  car.linksID + '">' + car.model + "     " + car.make + "     " + car.co2_emission + '</a>' + '<br>';
        }
        // change car.make to linksID, change query to include linksID, 
        // in app.route/hello/<linksID> go to database to get data to render template
        var car_co2_list = document.getElementById("car_list")
        car_co2_list.innerHTML = carlist;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}


function showEngineCars() {
    let url = getAPIBaseURL() + '/engine_size/';

    // Send the request to the books API / endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(cars) {
        // Add the <option> elements to the <select> element
        carlist = '';
        for (var k = 0; k<cars.length; k++) {
            var car = cars[k];
            carlist += '<a href="/api/hello/' +  car.linksID + '">' + car.model + "     " + car.make + "     " + car.engine_size + '</a>' + '<br>';
        }
        // change car.make to linksID, change query to include linksID, 
        // in app.route/hello/<linksID> go to database to get data to render template
        var car_fuel_list = document.getElementById("car_list")
        car_fuel_list.innerHTML = carlist;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}