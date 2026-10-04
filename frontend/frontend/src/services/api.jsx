const API_BASE_URL = "http://127.0.0.1:8000/api";

export async function getSummary() {
  const response = await fetch(`${API_BASE_URL}/analytics/summary`);

  if (!response.ok) {
    throw new Error("Failed to fetch summary data");
  }

  return response.json();
}

export async function getMonthlySales() {
  const response = await fetch(
    `${API_BASE_URL}/analytics/monthly-sales`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch monthly sales");
  }

  return response.json();
}

export async function getRegions() {
  const response = await fetch(
    `${API_BASE_URL}/analytics/regions`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch region data");
  }

  return response.json();
}

export async function getCategories() {
  const response = await fetch(
    `${API_BASE_URL}/analytics/categories`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch category data");
  }

  return response.json();
}

export async function getProducts() {
  const response = await fetch(
    `${API_BASE_URL}/analytics/products`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch product data");
  }

  return response.json();
}

export async function getAIInsights() {
  const response = await fetch(
    `${API_BASE_URL}/ai/insights`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch AI insights");
  }

  return response.json();
} 


export async function sendChatMessage(message) {
  const response = await fetch(
    "http://127.0.0.1:8000/api/ai/chat",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: message,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to send chat message");
  }

  return response.json();
}