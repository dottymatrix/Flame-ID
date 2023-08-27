// Import the Hedera SDK for JavaScript
const { HederaClient, AccountId, PrivateKey, TransferTransaction } = require("@hashgraph/sdk");

// Read and parse the JSON file that contains your data
const fs = require("fs");
const data = JSON.parse(fs.readFileSync("myData.json"));

// Define a function that takes a user query as a parameter and searches the JSON file for the matching data
function search() {
  // Get the user query from the input element
  let query = document.getElementById("query").value;

  // Filter the data array and return an array of objects that match the query
  let results = data.filter(function(obj) {
    // Loop through the properties of each object and check if any of them includes the query
    for (let prop in obj) {
      if (obj[prop].includes(query)) {
        // If yes, return true and add this object to the results array
        return true;
      }
    }
    // If no, return false and skip this object
    return false;
  });

  // Display the results in the app using another function
  display(results);

  // Send a transaction to Hedera using another function
  pay(query);
}

// Define a function that takes an array of objects as a parameter and displays the data in the app
function display(results) {
  // Get the results element from the HTML document
  let resultsElement = document.getElementById("results");

  // Clear any previous content from the results element
  resultsElement.innerHTML = "";

  // Check if there are any results
  if (results.length > 0) {
    // If yes, loop through the results array and create HTML elements for each object
    let list = results.map(function(obj) {
      // Create a div element with class "card"
      let card = document.createElement("div");
      card.className = "card";

      // Loop through the properties of each object and create p elements for each property-value pair
      for (let prop in obj) {
        let p = document.createElement("p");
        p.textContent = prop + ": " + obj[prop];
        // Append the p element to the card element
        card.appendChild(p);
      }

      // Return the card element
      return card;
    });

    // Append the list of card elements to the results element
    list.forEach(function(card) {
      resultsElement.appendChild(card);
    });
  } else {
    // If no, display a message that says "No results found"
    let p = document.createElement("p");
    p.textContent = "No results found";
    resultsElement.appendChild(p);
  }
}

// Define a function that takes a user query as a parameter and sends a transaction to Hedera to pay for the data
function pay(query) {
  // Create a new Hedera client and connect to the testnet
  const hederaClient = new HederaClient("testnet.hedera.com", "50211");

  // Specify your Hedera account ID and private key
  const myAccountId = AccountId.fromString("0.0.1234");
  const myPrivateKey = PrivateKey.fromString("302e020100300506032b6570042204206b9f6e6a5d0c1a1a9c06fe8d3cb1f6c2e782703df488fd29ad2c8d8ac7c8a4f3");

  // Specify the amount and the recipient of the transaction
  const amount = 1; // 1 Hbar for every 2 user queries
  const recipient = myAccountId; // Your Hedera account

  // Create a new transfer transaction and set the parameters
  const transaction = new TransferTransaction()
    .addHbarTransfer(myAccountId, -amount) // Send amount from your account
    .addHbarTransfer(recipient, amount) // Receive amount to your account
    .setMaxTransactionFee(100); // Set the maximum transaction fee

  // Sign the transaction with your private key or user's private key
  transaction.sign(myPrivateKey);

  // Execute the transaction and get the receipt
  const receipt = await transaction.execute(hederaClient);

  // Check if the transaction was successful
  if (receipt.status.toString() === "SUCCESS") {
    // If yes, display a message that says "Payment successful"
    console.log("Payment successful");
  } else {
    // If no, display a message that says "Payment failed"
    console.log("Payment failed");
  }
}
