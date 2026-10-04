import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function RegionChart({ data }) {
  return (
    <div className="chart-card">
      <h2>Sales by Region</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="region" />

          <YAxis />

          <Tooltip
            formatter={(value) =>
              `₹${Number(value).toLocaleString()}`
            }
          />

          <Bar dataKey="sales" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default RegionChart;