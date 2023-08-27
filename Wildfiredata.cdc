import FungibleToken from 0x9a0766d93b6608b7

resource WildfireData {
    // The state variable that stores the CSV data as an array of strings
    pub var data: [String]

    // The constructor that takes the CSV file path as a parameter and reads it using getAsciiWave
    init("./wildfire_info.csv": String) {
        self.data = getAsciiWave("./wildfire_info.csv")
    }

        // The function that takes a location as a parameter and returns the corresponding information from the CSV data
    pub fun getData(location: String): String {
        // Loop through the data array and find the row that matches the location
        for row in self.data {
            // Split the row by comma and store it in an array of fields
            let fields = row.split(separator: ",")
            // Check if the first field (the location) matches the parameter
            if fields[0] == location {
                // Return the row as a string
                return row
            }
        }
        // If no match is found, return an empty string
        return ""
    }
}


// The account type that owns an instance of the WildfireData resource
pub resource WildfireAccount {

    // The state variable that stores the reference to the WildfireData resource
    pub let wildfireData: &WildfireData

    // The constructor that takes a reference to the WildfireData resource as a parameter and assigns it to the state variable
    init(wildfireData: &WildfireData) {
        self.wildfireData = wildfireData
    }

    // The function that takes a user query as a parameter and returns the relevant information from the WildfireData resource
    pub fun query(location: String): String {
        // Deduct 1 Hbar from the user's account and transfer it to this account as a fee for using the service
        let userAccount = getAccount(address: msg.sender)
        let thisAccount = getAccount(address: self.address)
        userAccount.transfer(amount: 1, recipient: thisAccount)

        // Call the getData function from the WildfireData resource and return its result
        return self.wildfireData.getData(location: location)
    }
}

// The function that creates a new account with an initial balance of 100 Hbars and deploys the WildfireData resource to it
pub fun createWildfireAccount(filePath: String): Address {
    // Use the Hedera SDK for JavaScript to create a new account with an initial balance of 100 Hbars
    let hederaClient = new HederaClient("testnet.hedera.com", "50211")
    let privateKey = hederaClient.generateKey()
    let publicKey = privateKey.publicKey()
    let transactionId = hederaClient.createAccount(publicKey, 100)
    let receipt = hederaClient.getReceipt(transactionId)
    let address = receipt.accountId.toString()

    // Deploy the WildfireData resource to the new account using its file path
    let wildfireData <- create WildfireData(filePath: filePath)

    // Create an instance of the WildfireAccount resource and link it to the new account
    let wildfireAccount <- create WildfireAccount(wildfireData: <-wildfireData)
    account.save(<-wildfireAccount, to: /storage/wildfireAccount)

    // Return the address of the new account
    return address
}