"use strict";


// 1. isHometown
function isHomeTown(town) {
    return town === 'San Francisco';
}
// Define your function here


// 2. getFullName
function getFullName(firstName, lastName) {
    return `${firstName} ${lastName}`;
}
// Define your function here


// 3. calculateTotal
function calculateTotal(basePrice, state, tax=0.05) {
    const subtotal = basePrice * (1 + tax);
    let fee = 0;
    if (state === 'CA') {
        fee = 0.03 * subtotal;
    } else if (state === 'PA') {
        fee = 2;
    } else if (state === 'MA') {
        if (basePrice <= 100) {
            fee = 1;
        } else {
            fee = 3;
        }
    }
    return subtotal + fee;
}
// Define your function here


function test() {
    console.log("This is #1:");
    console.log(isHomeTown('San Francisco'));
    
    
    console.log("This is #2:");
    console.log(getFullName('Bob', 'The Builder'));

    console.log("This is #3:");
    console.log(calculateTotal(10, 'CA'));
}