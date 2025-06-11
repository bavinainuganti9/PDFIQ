import React, { useState } from "react";
import axios from "axios";

export default function QAInterface() {
  const [q, setQ] = useState("");
  const [ans, setAns] = useState("");
  const ask = async () => {
    const fd = new FormData();
    fd.append("question", q);
    const res = await axios.post("http://localhost:8000/qa/", fd);
    setAns(res.data.answer);
  };
  return (
    <div className="p-4">
      <textarea className="w-full h-20 border" value={q} onChange={e => setQ(e.target.value)} />
      <button onClick={ask} className="bg-blue-600 text-white px-4 py-2 mt-2">Ask</button>
      {ans && <div className="mt-4 p-2 border bg-gray-100 rounded">{ans}</div>}
    </div>
  );
}
