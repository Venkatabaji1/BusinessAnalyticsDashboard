import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function ProductChart({ data }) {
  return (
    <div className="chart-card">
      <h2>Top Products by Sales</h2>

      <ResponsiveContainer width="100%" height={320}>
        <BarChart
          data={data}
          layout="vertical"
          margin={{
            top: 10,
            right: 30,
            left: 30,
            bottom: 10,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis
            type="number"
            tickFormatter={(value) =>
              `₹${Number(value).toLocaleString()}`
            }
          />

          <YAxis
            type="category"
            dataKey="product"
            width={100}
          />

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

export default ProductChart;