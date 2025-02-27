# CDP Chatbot

A chatbot designed to answer questions about Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. The chatbot uses Natural Language Processing (NLP) to match user questions with relevant documentation and provides accurate responses.

---

## Features

- **Question Answering**: Ask questions about CDPs, and the chatbot will provide relevant answers.
- **Cross-CDP Comparison**: Compare features of different CDPs (e.g., "Compare Segment and mParticle").
- **Fallback Mechanism**: Handles irrelevant or out-of-scope questions gracefully.
- **User-Friendly Interface**: Simple and intuitive frontend interface for interacting with the chatbot.

---

## Tech Stack

### Frontend
- **React**: JavaScript library for building the user interface.
- **Axios**: For making HTTP requests to the backend.
- **CSS**: For styling the chatbot interface.

### Backend
- **Python**: Primary programming language.
- **Flask**: Web framework for creating the API.
- **Flask-CORS**: For handling Cross-Origin Resource Sharing (CORS).
- **Sentence-Transformers**: For generating sentence embeddings and computing similarity.
- **NumPy**: For numerical computations.
- **Regex**: For pattern matching in user questions.

---

## Data Structures and Algorithms (DSA)

### Frontend
- **State Management**: Using React's `useState` hook.
- **Event Handling**: Asynchronous HTTP requests with `async-await`.
- **Conditional Rendering**: Dynamically display responses and loading states.

### Backend
- **Data Structures**: Dictionaries, lists, and NumPy arrays.
- **Algorithms**:
  - Cosine similarity for matching user questions with documentation.
  - Regex for detecting cross-CDP comparison queries.
  - Linear search for finding the most relevant response.

---

## Installation and Setup

### Prerequisites
- **Node.js and npm** (for frontend)
- **Python 3.x** (for backend)
- **pip** (Python package manager)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cdp-chatbot.git
   cd cdp-chatbot/backend
2.Activate the virtual environment:

On macOS/Linux:
source venv/bin/activate

3.Install Python dependencies:
pip install flask flask-cors sentence-transformers numpy

4.Run the Flask server:
python app.py

The backend will start at http://127.0.0.1:5000.

Frontend Setup:
1.Navigate to the frontend directory:
cd ../frontend
2.Install Node.js dependencies:
npm install
3.npm start
