import { useEffect, useMemo, useState } from "react";
import axios from "axios";

export default function App() {
  const [rows, setRows] = useState([]);
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;

    (async () => {
      try {
        setLoading(true);
        const resp = await axios.get("/api/customers"); // proxied to FastAPI
        if (!alive) return;
        setRows(resp.data || []);
      } catch (e) {
        if (!alive) return;
        setErr(e?.response?.data?.detail || e?.message || "Failed to load customers");
      } finally {
        if (!alive) return;
        setLoading(false);
      }
    })();

    return () => {
      alive = false;
    };
  }, []);

  const columns = useMemo(() => {
    const set = new Set();
    for (const r of rows) Object.keys(r || {}).forEach((k) => set.add(k));
    return Array.from(set);
  }, [rows]);

  if (loading) return <div style={{ padding: 16 }}>Loading customers…</div>;
  if (err) return <div style={{ padding: 16, color: "crimson" }}>Error: {err}</div>;

  return (
    <div style={{ padding: 16 }}>
      <h1 style={{ marginBottom: 12 }}>Customers</h1>
      <div style={{ marginBottom: 12, color: "#666" }}>{rows.length} customers</div>

      <div style={{ overflow: "auto", border: "1px solid #ddd", borderRadius: 8 }}>
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14 }}>
          <thead>
            <tr>
              {columns.map((c) => (
                <th
  key={c}
  style={{
    position: "sticky",
    top: 0,
    background: "#1f2937",   // dark gray
    color: "#ffffff",        // white text
    borderBottom: "1px solid #111827",
    textAlign: "left",
    padding: "10px 8px",
    whiteSpace: "nowrap",
    fontWeight: 600,
  }}
>
                  {c}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((r, idx) => (
              <tr key={r.cid ?? idx} style={{ borderBottom: "1px solid #eee" }}>
                {columns.map((c) => (
                  <td key={c} style={{ padding: "8px", whiteSpace: "nowrap" }}>
                    {formatCell(r?.[c])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function formatCell(v) {
  if (v === null || v === undefined) return "";
  if (typeof v === "boolean") return v ? "true" : "false";
  if (typeof v === "object") return JSON.stringify(v);
  return String(v);
}
