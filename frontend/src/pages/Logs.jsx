import { useEffect, useState } from "react";
import api from "../api/axios";

function Logs() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    const res = await api.get("activity-logs/");
    setLogs(res.data.results);
  };

  return (
    <div>
      <h2>Activity Logs</h2>
      {logs.map((log) => (
        <div key={log.id}>
          {log.action} - {log.object_repr}
        </div>
      ))}
    </div>
  );
}

export default Logs;