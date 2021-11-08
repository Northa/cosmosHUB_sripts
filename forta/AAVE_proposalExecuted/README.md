# AAVE Proposal Execution event listener

## Description

This agent detects transactions to AaveGovernanceV2 mainnet contract and awaits ProposalExecuted event.
Once ProposalExecuted event found the alert triggers.

## Supported Chains

- Ethereum

## Alerts

  - name "Aave Governance proposal event Listener"
  - description "Proposal executed. proposal_id: {id} Initiator: {Initiator addr}"
  - alert_id "AaveProposalExec"
  - type is always set to "Info"
  - severity is always set to "Info".
  - metadata "blocknumber" field contains block number

## Test Data

The agent behaviour can be verified with the following transactions:

- 0x56b5694adad6994206dae5573ecb78530a11fd50fde37aa996375c7bb3a70b0f block 13474128
- 0xc78cedcdc84fc0b9a19e09ab16471cffcc572eb58ee33082a6da1492d128cffc block 13426219
- 0x50110967aa7137c493ce8c258388f76458bfe9beecd6d3b5da1f32015297c5fd block 13381378

###### Examples

`$ npm run tx 0x55390f9ad5c1b325bc32f10f24c5a75d34a9d79869512f56ad95987044686ca1`

`$ npm run block 13534152`

