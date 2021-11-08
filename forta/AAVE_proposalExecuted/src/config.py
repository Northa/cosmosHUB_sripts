from json import loads
import requests
AaveGovernanceV2_MAINNET = f'0xEC568fffba86c094cf06b22134B23074DFE2252c'.lower()
AaveGovernanceV2_ABI_MAINNET = f"https://api.etherscan.io/api?module=contract&action=" \
                               f"getabi&address={AaveGovernanceV2_MAINNET}"

#decided to provide precompilled abi in order to save time
abi = """{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},""" \
      """{\"indexed\":true,\"internalType\":\"address\",\"name\":\"initiatorExecution\",\"type\":\"address\"}],\"name\":\"ProposalExecuted\",\"type\":\"event\"}"""


def get_ABI() -> str:
    """returns proposalExecuted abi from etherscan"""
    response = requests.get(AaveGovernanceV2_ABI_MAINNET)
    response = loads(loads(response.text)['result'])
    for event in response:
        if event['type'] == 'event' and event['name'] == 'ProposalExecuted':
            event = str(event).replace("'", '\"').replace('False', 'false').replace('True', 'true')
            return event
