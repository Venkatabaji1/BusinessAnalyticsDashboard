import { useEffect, useState } from "react";

import KPICard from "./components/KPICard";
import MonthlySalesChart from "./components/MonthlySalesChart";
import RegionChart from "./components/RegionChart";
import CategoryChart from "./components/CategoryChart";
import ProdcutChart from "./components/ProdcutChart";
import AIInsights from "./components/AIInsights";
import AIChat from "./components/AIChat";

import {
  getSummary,
  getMonthlySales,
  getRegions,
  getCategories,
  getProducts,
  getAIInsights,
} from "./services/api";

import "./App.css";

function App() {
  const [summary, setSummary] = useState(null);
  const [monthlySales, setMonthlySales] = useState([]);
  const [regions, setRegions] = useState([]);
  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);
  const [insights, setInsights] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [
          summaryData,
          monthlyData,
          regionData,
          categoryData,
          productData,
          aiData,
        ] = await Promise.all([
          getSummary(),
          getMonthlySales(),
          getRegions(),
          getCategories(),
          getProducts(),
          getAIInsights(),
        ]);

        setSummary(summaryData);
        setMonthlySales(monthlyData);
        setRegions(regionData);
        setCategories(categoryData);
        setProducts(productData);
        setInsights(aiData.insights);
      } catch (error) {
        console.error("Dashboard loading error:", error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loading-box">
          <div className="loading-spinner"></div>
          <h2>Loading Dashboard</h2>
          <p>Preparing your business analytics...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      {/* TOP HEADER */}
      <header className="top-header">
        <div className="brand">
          <div className="brand-icon">✦</div>

          <div>
            <h1>InsightHub</h1>
            <span>Business Intelligence</span>
          </div>
        </div>

        <div className="header-status">
          <span className="status-dot"></span>
          AI Connected
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="dashboard-container">

        {/* HERO */}
        <section className="hero-section">
          <div>
            <span className="eyebrow">BUSINESS ANALYTICS</span>

            <h2>
              Business <span>Overview</span>
            </h2>

            <p>
              Monitor sales performance, discover trends and get
              AI-powered business insights.
            </p>
          </div>

          <div className="hero-badge">
            <div className="hero-badge-icon">✦</div>

            <div>
              <strong>AI Powered</strong>
              <span>Real-time business analysis</span>
            </div>
          </div>
        </section>

        {/* KPI CARDS */}
        <section className="kpi-grid">

          <KPICard
            title="Total Sales"
            value={`₹${Number(
              summary?.total_sales || 0
            ).toLocaleString()}`}
            description="Overall revenue generated"
            icon="₹"
            type="sales"
          />

          <KPICard
            title="Total Profit"
            value={`₹${Number(
              summary?.total_profit || 0
            ).toLocaleString()}`}
            description={`${summary?.profit_margin || 0}% profit margin`}
            icon="↗"
            type="profit"
          />

          <KPICard
            title="Total Orders"
            value={summary?.total_orders || 0}
            description="Orders processed"
            icon="◫"
            type="orders"
          />

          <KPICard
            title="Units Sold"
            value={summary?.total_quantity || 0}
            description="Products sold"
            icon="▦"
            type="units"
          />

        </section>

        {/* ANALYTICS HEADER */}
        <div className="section-heading">
          <div>
            <span>PERFORMANCE</span>
            <h3>Sales Analytics</h3>
          </div>

          <div className="data-live">
            <span></span>
            Live Data
          </div>
        </div>

        {/* MONTHLY SALES */}
        <section className="chart-full">
          <div className="chart-heading">
            <div>
              <span className="chart-label">REVENUE TREND</span>
              <h3>Monthly Sales</h3>
            </div>

            <div className="chart-total">
              <span>Total</span>
              <strong>
                ₹{Number(
                  summary?.total_sales || 0
                ).toLocaleString()}
              </strong>
            </div>
          </div>

          <MonthlySalesChart data={monthlySales} />
        </section>

        {/* REGION + CATEGORY */}
        <section className="two-column-grid">

          <div className="chart-card-modern">
            <div className="chart-heading">
              <div>
                <span className="chart-label">GEOGRAPHY</span>
                <h3>Sales by Region</h3>
              </div>
            </div>

            <RegionChart data={regions} />
          </div>

          <div className="chart-card-modern">
            <div className="chart-heading">
              <div>
                <span className="chart-label">PRODUCT MIX</span>
                <h3>Sales by Category</h3>
              </div>
            </div>

            <CategoryChart data={categories} />
          </div>

        </section>

        {/* PRODUCTS */}
        <section className="chart-full product-section">
          <div className="chart-heading">
            <div>
              <span className="chart-label">TOP PERFORMERS</span>
              <h3>Top Products by Sales</h3>
            </div>
          </div>

          <ProdcutChart data={products} />
        </section>

        {/* AI SECTION */}
        <div className="section-heading ai-section-heading">
          <div>
            <span>ARTIFICIAL INTELLIGENCE</span>
            <h3>Business Intelligence</h3>
          </div>
        </div>

        <section className="ai-layout">

          {/* AI INSIGHTS */}
          <div className="insights-wrapper">
            <AIInsights insights={insights} />
          </div>

          {/* AI CHAT */}
          <div className="chat-wrapper">
            <AIChat />
          </div>

        </section>

        {/* FOOTER */}
        <footer className="footer">
          <div>
            <strong>InsightHub</strong>
            <span>Business Analytics Platform</span>
          </div>

          <span>
            Powered by Python • React • Gemini AI
          </span>
        </footer>

      </main>
    </div>
  );
}

export default App;