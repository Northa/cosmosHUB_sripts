from forta_agent import Finding, FindingType, FindingSeverity
from .config import AaveGovernanceV2_MAINNET, abi


def handle_transaction(transaction_event):

    findings = []
    if transaction_event.to != AaveGovernanceV2_MAINNET:
        return findings
    events = transaction_event.filter_log(abi, AaveGovernanceV2_MAINNET)

    for event in events:
        findings.append(Finding({
            'name': 'Aave Governance proposal event Listener',
            'description': f"Proposal executed. "
            f"proposal_id: {event.get('args')['id']} "
            f"Initiator: {event.get('args')['initiatorExecution']}",
            'proposal_id': event.get('args')['id'],
            'alert_id': 'AaveProposalExec',
            'type': FindingType.Info,
            'blocknumber': event.get('blockNumber'),
            'severity': FindingSeverity.Info,
            'metadata': {'blocknumber': event.get('blockNumber')}
        }))

    return findings
