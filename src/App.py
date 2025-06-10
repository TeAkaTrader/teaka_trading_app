import React, { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState<any>(null);

  useEffect(() => {
    fetch("https://api.teaka.trading/ev_remote/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ cmd: "status" }),
    })
      .then((res) => res.json())
      .then((data) => setStatus(data));
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "monospace", background: "#111", color: "#0f0" }}>
      <h1>🧠 EV Firemind Dashboard</h1>
      {status ? (
        <pre>{JSON.stringify(status, null, 2)}</pre>
      ) : (
        <p>Loading status from EV Core...</p>
      )}
    </div>
  );
}

export default App;
