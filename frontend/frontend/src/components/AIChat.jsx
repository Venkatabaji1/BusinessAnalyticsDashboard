import { useState } from "react";
import { sendChatMessage } from "../services/api";

function AIChat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend(text = message) {
    const userMessage = text.trim();

    if (!userMessage || loading) {
      return;
    }

    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        text: userMessage,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const data = await sendChatMessage(userMessage);

      setMessages((previous) => [
        ...previous,
        {
          role: "ai",
          text: data.response,
        },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setMessages((previous) => [
        ...previous,
        {
          role: "ai",
          text: "Unable to connect to the AI assistant. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  }

  const suggestions = [
    "What is our total sales?",
    "Which region has the highest sales?",
    "Which product performs best?",
    "How can we improve profit?",
  ];

  return (
    <div className="ai-chat-card">

      {/* HEADER */}
      <div className="ai-chat-top">

        <div className="ai-chat-title">

          <div className="ai-logo">
            ✦
          </div>

          <div>
            <h3>AI Business Assistant</h3>
            <span>
              Ask questions about your business
            </span>
          </div>

        </div>

        <div className="ai-online">
          <span></span>
          Online
        </div>

      </div>

      {/* CHAT BODY */}
      <div className="chat-messages">

        {messages.length === 0 && (
          <div className="chat-welcome">

            <div className="welcome-icon">
              ✦
            </div>

            <h3>
              How can I help?
            </h3>

            <p>
              Ask me about sales, products,
              regions, profit or business trends.
            </p>

            <div className="suggested-questions">

              {suggestions.map((question) => (
                <button
                  key={question}
                  onClick={() => setMessage(question)}
                >
                  {question}
                  <span>→</span>
                </button>
              ))}

            </div>

          </div>
        )}

        {messages.map((item, index) => (
          <div
            key={index}
            className={`chat-message ${item.role}`}
          >

            {item.role === "ai" && (
              <div className="message-ai-icon">
                ✦
              </div>
            )}

            <div className="message-content">

              <span className="message-label">
                {item.role === "user"
                  ? "You"
                  : "AI Assistant"}
              </span>

              <div className="message-bubble">
                {item.text}
              </div>

            </div>

          </div>
        ))}

        {loading && (
          <div className="chat-message ai">

            <div className="message-ai-icon">
              ✦
            </div>

            <div className="message-content">

              <span className="message-label">
                AI Assistant
              </span>

              <div className="message-bubble typing">
                <span></span>
                <span></span>
                <span></span>
              </div>

            </div>

          </div>
        )}

      </div>

      {/* INPUT */}
      <div className="chat-input-wrapper">

        <textarea
          value={message}
          onChange={(event) =>
            setMessage(event.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Ask about your sales data..."
          rows={1}
          disabled={loading}
        />

        <button
          className="send-button"
          onClick={() => handleSend()}
          disabled={!message.trim() || loading}
        >
          →
        </button>

      </div>

      <div className="chat-footer">
        AI responses are based on your business data
      </div>

    </div>
  );
}

export default AIChat;