class Settings: 
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._settings = {
                'suspicious_domains': ['phishing.com', 'malicious.com'],
                'urgent_keywords': ['urgent', 'immediate', 'action required']
            }
        return cls._instance

    def get_setting(self, key):
        return self.__class__._settings.get(key)
