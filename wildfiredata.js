// Import the Hedera SDK for JavaScript
const { HederaClient, AccountId, PrivateKey, ContractExecuteQuery } = require("@hashgraph/sdk");

// Create a new Hedera client and connect to the testnet
const hederaClient = new HederaClient("testnet.hedera.com", "50211");

// Specify the contract address of your smart contract
const contractAddress = "0x123456789abcdef";

// Specify the location you want to query
const location = "Toronto";

// Create a new contract execute query and set the parameters
const query = new ContractExecuteQuery()
    .setContractId(contractAddress)
    .setGas(100000)
    .setFunction("query", [location]);

// Sign the query with your private key or user's private key
const privateKey = PrivateKey.fromString("302e020100300506032b6570042204206b9f6e6a5d0c1a1a9c06fe8d3cb1f6c2e782703df488fd29ad2c8d8ac7c8a4f3");
query.sign(privateKey);

// Execute the query and get the result
const result = await query.execute(hederaClient);

// Print the result as a string
console.log(result.toString());
