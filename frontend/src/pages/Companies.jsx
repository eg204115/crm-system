import { useEffect, useState } from "react";
import api from "../api/axios";

function Companies() {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    fetchCompanies();
  }, []);

  const fetchCompanies = async () => {
    const res = await api.get("companies/");
    setCompanies(res.data.results);
  };

  return (
    <div>
      <h2>Companies</h2>
      {companies.map((c) => (
        <div key={c.id}>
          {c.name} - {c.industry}
        </div>
      ))}
    </div>
  );
}

export default Companies;