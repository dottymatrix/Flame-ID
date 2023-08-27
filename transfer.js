const { Client, PrivateKey, AccountCreateTransaction, AccountBalanceQuery, Hbar, TransferTransaction } = require("@hashgraph/sdk");
require('dotenv').config();

async function Environment() {

    //Grab your Hedera testnet account ID and private key from your .env file
    const myAccountId = process.env.HEDERA_ACCOUNT_ID;
    const myPrivateKey = process.env.HEDERA_PRIVATE_KEY;

    // If we weren't able to grab it, we should throw a new error
    if (!myAccountId || !myPrivateKey) {
        throw new Error("Environment variables MY_ACCOUNT_ID and MY_PRIVATE_KEY must be present");
    }

    //Create your Hedera Testnet client
    const client = Client.forTestnet();

    //Set your account as the client's operator
    client.setOperator(myAccountId, myPrivateKey);

    //Set the default maximum transaction fee & max query payment (in Hbar)
    client.setDefaultMaxTransactionFee(new Hbar(1000));
    client.setMaxQueryPayment(new Hbar(1000));

    const newAccountId = "0.0.1071948";

    //Create the transfer transaction
    const sendHbar = await new TransferTransaction()
        .addHbarTransfer(myAccountId, Hbar.fromTinybars(-100)) //Sending account
        .addHbarTransfer(newAccountId, Hbar.fromTinybars(100)) //Receiving account
        .execute(client);

    //Verify the transaction reached consensus
    const transactionReceipt = await sendHbar.getReceipt(client);
    console.log("The transfer transaction from my account to the new account was: " + transactionReceipt.status.toString());

    const TransactionRx = await sendHbar.getReceipt(client);
    console.log("Status of txn:" +(TransactionRx.status));
    
    //check the account's new balance
    const getNewBalance = await new AccountBalanceQuery()
        .setAccountId(newAccountId)
        .execute(client);

    console.log("New balance:" +(getNewBalance.hbars.toTinybars()));

    client.close();
}
Environment();