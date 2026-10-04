function AIInsights({ insights }) {
  return (
    <div className="ai-insights-card">
      <div className="ai-insights-header">
        <div>
          <h2>AI Business Insights</h2>
          <p>
            AI-generated analysis based on your sales data
          </p>
        </div>
      </div>

      <div className="ai-insights-content">
        {insights ? (
          <p>{insights}</p>
        ) : (
          <p>No AI insights available.</p>
        )}
      </div>
    </div>
  );
}

export default AIInsights;