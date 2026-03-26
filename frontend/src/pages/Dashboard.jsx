import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <Link to="/companies">Companies</Link>
      <br />
      <Link to="/logs">Activity Logs</Link>
    </div>
  );
}

export default Dashboard;