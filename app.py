from flask import Flask, render_template, request, redirect, url_for, jsonify # type: ignore
from detector.rule_factory import RuleFactory
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

def check_email(email):
    rules = ["suspicious_links", "sender_address", "urgent_language"]
    results = {}

    for rule_type in rules:
        rule = RuleFactory.get_rule(rule_type)
        results[rule_type] = rule.check(email)

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'clear' in request.form:
            return redirect(url_for('index'))

        email = {
            'from': request.form['from'],
            'subject': request.form['subject'],
            'body': request.form['body']
        }
        results = check_email(email)
        return render_template('index.html', email=email, results=results)

    return render_template('index.html', email=None, results=None)

@app.route('/detect', methods=['POST'])
def detect_phishing():
    data = request.get_json()
    email_text = {
        'from': data.get('from'),
        'subject': data.get('subject'),
        'body': data.get('body')
    }

    results = check_email(email_text)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
