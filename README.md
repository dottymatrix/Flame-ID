# Flame-ID 
A blockchain Dapp for real-time wildfire data and alerts.

## Inspiration ✨
Flame-ID aims to contribute to the UN goal 11: Sustainable Cities and Communities, by making cities and human settlements inclusive, safe, resilient, and sustainable. The project was created to address multiple accomplishments in one go: sustainability and blockchain sponsor tools. It is an ambitious vision to demonstrate blockchain utility, while highlighting a UN sustainability goal. Flame ID is part of a larger mission to keep humanity on a prosperous trajectory into the future. When we take action to solve our problems, we are taking the responsibility to ensure a brighter future for all. 

## What it does 💡 
Flame ID is a Dapp that provides users with real-time data and alerts on wildfire risk and activity. 

## How we built it 🪄
Using the Hedera Mirror Node API and the Flow Access API. The app uses JavaScript, the Hedera SDK, and the Flow JS SDK to query data from the blockchain. The BC Wildfire Service resources are sources for information on fire bans, restrictions, legislation, and regulations. We wrote a Python webscraping app to pull relevant Fire data from the web to be organized in a CSV file or readable format for the blockchain smart contract application. This application will be able to parse the data and write it back to our User interface with the relevant Javascript SDK and our HTML and CSS front end dashboard.
