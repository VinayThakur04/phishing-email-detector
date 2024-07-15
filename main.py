from detector.rule_factory import RuleFactory

def main():
    email = {
        'from': 'phisher@example.com',
        'subject': 'Urgent: Verify Your Account',
        'body': 'Please click the link to verify your account: http://phishing.com/verify'
    }

    rules = ["suspicious_links", "sender_address", "urgent_language"]
    results = {}

    for rule_type in rules:
        rule = RuleFactory.get_rule(rule_type)
        results[rule_type] = rule.check(email)

    for rule, found in results.items():
        if found:
            print(f"Phishing detected by rule: {rule}")
        else:
            print(f"No phishing detected by rule: {rule}")

if __name__ == "__main__":
    main()
