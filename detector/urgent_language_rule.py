from .base_rule import BaseRule
from config.settings import Settings

class UrgentLanguageRule(BaseRule):
    def check(self, email: dict) -> bool:
        settings = Settings()
        urgent_keywords = settings.get_setting('urgent_keywords')
        subject_and_body = email['subject'] + ' ' + email['body']
        for keyword in urgent_keywords:
            if keyword in subject_and_body.lower():
                return True
        return False
