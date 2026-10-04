function KPICard({
  title,
  value,
  description,
  icon,
  type,
}) {
  return (
    <div className={`kpi-card ${type}`}>
      <div className="kpi-top">
        <div className="kpi-icon">
          {icon}
        </div>

        <span className="kpi-status">●</span>
      </div>

      <div className="kpi-content">
        <p>{title}</p>

        <h2>{value}</h2>

        <span>{description}</span>
      </div>
    </div>
  );
}

export default KPICard;