from .suspicious_links_rule import SuspiciousLinksRule
from .sender_address_rule import SenderAddressRule
from .urgent_language_rule import UrgentLanguageRule

class RuleFactory:
    @staticmethod
    def get_rule(rule_type: str):
        if rule_type == 'suspicious_links':
            return SuspiciousLinksRule()
        elif rule_type == 'sender_address':
            return SenderAddressRule()
        elif rule_type == 'urgent_language':
            return UrgentLanguageRule()
        else:
            raise ValueError(f"Unknown rule type: {rule_type}")
