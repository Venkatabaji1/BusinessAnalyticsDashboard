import {
  PieChart,
  Pie,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

function CategoryChart({ data }) {
  return (
    <div className="chart-card">
      <h2>Sales by Category</h2>

      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie
            data={data}
            dataKey="sales"
            nameKey="category"
            cx="50%"
            cy="50%"
            outerRadius={100}
            label
          />

          <Tooltip
            formatter={(value) =>
              `₹${Number(value).toLocaleString()}`
            }
          />

          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default CategoryChart;