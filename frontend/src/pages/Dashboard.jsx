import { useEffect, useState } from "react";
import api from "../services/api";
import "./Dashboard.css";

export default function Dashboard() {
  const [dashboard, setDashboard] = useState(null);

  const loadDashboard = async () => {
    try {
      const res = await api.get("/jobs/dashboard");
      setDashboard(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadDashboard();

    const interval = setInterval(loadDashboard, 5000);

    return () => clearInterval(interval);
  }, []);

  if (!dashboard)
    return <h1 className="loading">Loading...</h1>;

  return (
    <div className="dashboard">

      <h1 className="title">
          Job Monitoring Dashboard
      </h1>

      <div className="cards">

        <div className="card">
          <h3>Total Jobs</h3>
          <h2>{dashboard.total_jobs}</h2>
        </div>

        <div className="card">
          <h3>Pending</h3>
          <h2>{dashboard.pending_jobs}</h2>
        </div>

        <div className="card">
          <h3>Running</h3>
          <h2>{dashboard.running_jobs}</h2>
        </div>

        <div className="card">
          <h3>Completed</h3>
          <h2 className="high">{dashboard.completed_jobs}</h2>
        </div>

        <div className="card">
          <h3>Failed</h3>
          <h2 className="low">{dashboard.failed_jobs}</h2>
        </div>

      </div>

      <div className="section">

        <h2>Queue Statistics</h2>

        <div className="stats">

          <div className="stat-box">
            <h3>High Priority</h3>
            <h2 className="high">
              {dashboard.queue_statistics.high}
            </h2>
          </div>

          <div className="stat-box">
            <h3>Medium Priority</h3>
            <h2 className="medium">
              {dashboard.queue_statistics.medium}
            </h2>
          </div>

          <div className="stat-box">
            <h3>Low Priority</h3>
            <h2 className="low">
              {dashboard.queue_statistics.low}
            </h2>
          </div>

        </div>

      </div>

      <div className="average">
        <h2>Average Processing Time</h2>
        <h1>
          {dashboard.average_processing_time_seconds} sec
        </h1>
      </div>

    </div>
  );
}