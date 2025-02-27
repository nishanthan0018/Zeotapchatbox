from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, util
import numpy as np
import re

app = Flask(__name__)
CORS(app)

# Load Sentence Transformer Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Expanded Documentation for CDPs
documentation = {
    "Segment": [
        "To set up a new source in Segment, go to the Sources tab and click 'Add Source'.",
        "To track events in Segment, use the 'track' API method with event properties.",
        "You can send data from Segment to destinations using the 'Connections' feature."
    ],
    "mParticle": [
        "To create a user profile in mParticle, navigate to the Profiles section.",
        "mParticle allows you to set up event forwarding to multiple destinations.",
        "Use the 'Audience' feature to create user segments in mParticle."
    ],
    "Lytics": [
        "To build an audience segment in Lytics, use the Audience Builder tool.",
        "Lytics allows you to integrate customer data from multiple sources.",
        "You can use Lytics for personalized content recommendations."
    ],
    "Zeotap": [
        "To integrate your data with Zeotap, follow the API documentation provided.",
        "Zeotap provides identity resolution and enrichment features for customer data.",
        "You can create audience segments in Zeotap and activate them in different platforms."
    ]
}

# Flatten the documentation into sentences
doc_sentences = [sentence for sentences in documentation.values() for sentence in sentences]
doc_embeddings = model.encode(doc_sentences, convert_to_tensor=True)

# Extract CDP names
cdp_names = list(documentation.keys())

# Handle irrelevant or out-of-scope questions
def is_irrelevant(question):
    unrelated_keywords = ["movie", "weather", "sports", "news", "game"]
    return any(keyword in question.lower() for keyword in unrelated_keywords)

@app.route('/ask', methods=['POST', 'OPTIONS'])
def ask():
    if request.method == 'OPTIONS':
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    user_question = request.json.get('question')

    # Handle out-of-scope questions
    if is_irrelevant(user_question):
        return jsonify({"response": "I'm here to answer questions about CDPs like Segment, mParticle, Lytics, and Zeotap."})

    # Detect Cross-CDP Comparison
    comparison_match = re.search(r"(compare|difference between) (\w+) and (\w+)", user_question, re.IGNORECASE)
    if comparison_match:
        cdp1, cdp2 = comparison_match.group(2), comparison_match.group(3)
        if cdp1 in documentation and cdp2 in documentation:
            return jsonify({"response": f"Here are some key differences:\n- {cdp1}: {documentation[cdp1][0]}\n- {cdp2}: {documentation[cdp2][0]}"})
        return jsonify({"response": "I can only compare Segment, mParticle, Lytics, and Zeotap."})

    # Encode the user question
    question_embedding = model.encode(user_question, convert_to_tensor=True)

    # Compute similarity scores
    similarities = util.pytorch_cos_sim(question_embedding, doc_embeddings)[0].cpu().numpy()

    # Get the best match
    most_similar_index = np.argmax(similarities)
    best_score = similarities[most_similar_index]
    most_similar_sentence = doc_sentences[most_similar_index]

    # If similarity score is too low, return a fallback response
    if best_score < 0.5:
        return jsonify({"response": "I couldn't find a perfect match. Try rephrasing your question!"})

    # Identify which CDP the response belongs to
    matched_cdp = next(cdp for cdp in cdp_names if most_similar_sentence in documentation[cdp])

    return jsonify({
        "response": most_similar_sentence,
        "cdp": matched_cdp,
        "confidence": float(best_score)  # Convert numpy float to Python float
    })

if __name__ == '__main__':
    app.run(debug=True)