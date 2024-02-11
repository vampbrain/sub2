from flask import Flask, request, jsonify
from nlp import analyze_sentiment, detect_dark_patterns

app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_route():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Text key is missing'}), 400
    text = data['text']
    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

@app.route('/detect_dark_patterns', methods=['POST'])
def detect_dark_patterns_route():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Text key is missing'}), 400
    text = data['text']
    dark_patterns = detect_dark_patterns(text)
    return jsonify({'dark_patterns': dark_patterns})

if __name__ == '__main__':
    app.run(debug=True)
