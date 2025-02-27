// import { useState } from "react";
// import axios from "axios";

// const Chatbot = () => {
//   const [question, setQuestion] = useState("");
//   const [response, setResponse] = useState("");
//   const [loading, setLoading] = useState(false);

//   const handleAsk = async () => {
//     if (!question.trim()) return;
//     setLoading(true);
//     try {
//       const res = await axios.post("http://127.0.0.1:5000/ask", { question });
//       setResponse(res.data.response);
//     } catch (error) {
//       console.error("Error:", error);
//       setResponse("Something went wrong. Please try again.");
//     }
//     setLoading(false);
//   };

//   return (
//     <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
//       <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
//         <h2 className="text-xl font-bold mb-4">CDP Chatbot</h2>
//         <textarea
//           className="w-full border p-2 rounded-md"
//           rows="3"
//           placeholder="Ask something..."
//           value={question}
//           onChange={(e) => setQuestion(e.target.value)}
//         />
//         <button
//           onClick={handleAsk}
//           className="bg-blue-500 text-white px-4 py-2 rounded-md mt-3 w-full"
//           disabled={loading}
//         >
//           {loading ? "Thinking..." : "Ask"}
//         </button>
//         {response && (
//           <div className="mt-4 p-3 border rounded bg-gray-50">
//             <strong>Chatbot:</strong> {response}
//           </div>
//         )}
//       </div>
//     </div>
//   );
// };

// export default Chatbot;
import { useState } from "react";
import axios from "axios";
import "./App.css"; // Import CSS file

const Chatbot = () => {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5000/ask", { question });
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Something went wrong. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="chatbot-container">
      <h2 className="chatbot-title">CDP Chatbot</h2>
      <textarea
        className="chatbot-input"
        rows="3"
        placeholder="Ask something..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button
        onClick={handleAsk}
        className="chatbot-button"
        disabled={loading}
      >
        {loading ? "Thinking..." : "Ask"}
      </button>
      {response && (
        <div className="chatbot-response">
          <strong>Chatbot:</strong> {response}
        </div>
      )}
    </div>
  );
};

export default Chatbot;