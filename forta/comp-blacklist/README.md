# Compound blacklisted addrs tracker Agent

## Description

This agent detects transactions from blacklisted addresses to Compound Comptroller contract

## Supported Chains

- Ethereum

## Alerts

- COMP-blacklist-1
  - name "Blacklisted alert"
  - description "INFO {addr} {comment when and where addr was involved in fraud}"
  - alert_id "COMP-blacklist-1"
  - type is always set to "Suspicious"
  - severity is always set to "Critical". We don't want to deal with scammers/phishers!
  - metadata "gas_used" field contains amount of gas used


## Test Data

##### As a test, we added two random addresses to the list which iteracted with COMP contract recently.
##### These addresses are not related to any scam/phishing :) It's just for a test!

The agent behaviour can be verified with the following transactions:

- 0x1b5badbb20dc6d990c98dec20c2fe1937c46ae1cf73db753902e4387db50d415 block 13464199
- 0xd5ee4032f670e12f1696c99c8c80dc87e89bbb99ed7b11a7e2e98ed08a2f0797 block 13464516
- 0xb4f894f692681d7773551761d2e96af8e5b072de968a6d2a3f29cde4c59e4fb4 block 13463656

###### Examples

`$ npm run tx 0xb4f894f692681d7773551761d2e96af8e5b072de968a6d2a3f29cde4c59e4fb4`

`$ npm run block 13463656`

![test](https://raw.githubusercontent.com/Northa/cosmosHUB_sripts/main/forta/comp-blacklist/screen/screen1.png)
