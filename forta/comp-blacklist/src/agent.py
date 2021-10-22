import requests
from json import loads
from forta_agent import Finding, FindingType, FindingSeverity
from .config import COMPOUND_COMPTROLLER_ADDRESS, DARKLIST, TEST_ADDRS


def get_blacklisted() -> list:
    """get a blacklisted addrs from MEW github"""
    response = loads(requests.get(DARKLIST).text)
    response.extend(TEST_ADDRS)
    return response


def handle_transaction(transaction_event) -> list:
    """
    Checking if recipient address == contract.
    If not return empty list
    Else check whether the sender's address on the blacklist
    """
    findings = []
    if transaction_event.to != COMPOUND_COMPTROLLER_ADDRESS:
        return findings

    BLACKLISTED = get_blacklisted()

    for addr in BLACKLISTED:

        if addr['address'].lower() == transaction_event.from_:
            findings.append(Finding({
                'name': 'Blacklisted alert',
                'description': f"INFO: {addr['address']} {addr['comment']}",
                'alert_id': 'COMP-blacklist-1',
                'type': FindingType.Suspicious,
                'severity': FindingSeverity.Critical,
                'metadata': {
                    'gas_used': f"{transaction_event.gas_used}"
                }
            }))

    return findings
