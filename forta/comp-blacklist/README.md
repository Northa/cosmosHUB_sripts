# Compound blacklisted addrs tracker Agent

## Description

This agent detects transactions from blacklisted addresses to Compound contract

## Supported Chains

- Ethereum

## Alerts

- COMP-blacklist-1
  - Severity is always set to "Critical". We don't want to deal with scammers/phishers!
  - Type is always set to "Suspicious"
  - Metadata "gas_used" field contains amount of gas used

## Test Data

##### As a test, we added two random addresses to the list which iteracted with COMP contract recently.
##### These addresses are not related to any scam/phishing :) It's just for a test!

The agent behaviour can be verified with the following transactions:

- 0xa6a9a16107976125ff0cb5f141dd99bc68d351f6798fcec2e2924529f10def2a block 13460264
- 0x009feaa0d726d1a88433d6e3b8c8cb247636f2f0f0b7ead0b685802a62a2f8c8 block 13460200

###### Examples

`$ npm run tx 0xa6a9a16107976125ff0cb5f141dd99bc68d351f6798fcec2e2924529f10def2a`

`$ npm run block 13460264`
