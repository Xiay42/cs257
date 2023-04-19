// CS257 end-to-end assignment
// written by Yiming Xia
// 11.9.2022

window.onload = initialize;

function initialize() {
    var button = document.getElementById("searchButton");
    button.onclick = showCars;

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

function showCars() {
    let searchString = document.getElementById("searchString").value;
    let url = getAPIBaseURL() + '/search/' + searchString;

    // Send the request to the books API / endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(cars) {
        carlist = '';
        if (cars.length !== 0) {
            // Add the <option> elements to the <select> element
            carlist += '<p1>The following list is in the format: carModel, carMake, co2Emission</p1><br>';
            for (var k = 0; k<cars.length; k++) {
                var car = cars[k];
                carlist += '<a href="/api/hello/' +  car.linksID + '">' + car.model + ', ' + car.make + ', ' + car.co2 + '<td>' + '</tr>' + '<br>';
                // carlist += '<tr href="/api/hello/' + car.linksID + '">' + '<td>' + car.model + '</td><td>' + car.make + '</td><td>' + car.co2 + '</td>' + '</tr>'
            }
        }
        else {
            carlist += '<p>This is not a valid car model, please search something else, like honda or audi or benz.</p>';
        }
        var carlist_by_make = document.getElementById("carlist_by_make")
        carlist_by_make.innerHTML = carlist;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}
