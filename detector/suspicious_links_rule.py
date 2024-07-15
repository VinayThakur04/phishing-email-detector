import re
from .base_rule import BaseRule
from config.settings import Settings

class SuspiciousLinksRule(BaseRule):
    def check(self, email: dict) -> bool:
        settings = Settings()
        suspicious_domains = settings.get_setting('suspicious_domains')

        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = url_pattern.findall(email['body'])

        for url in urls:
            for domain in suspicious_domains:
                if domain in url:
                    return True
        return False
