import React, { useState } from "react";
import axios from "axios";

export default function Uploader({ onUpload }) {
  const [file, setFile] = useState(null);
  const upload = async () => {
    const fd = new FormData();
    fd.append("file", file);
    await axios.post("http://localhost:8000/upload/", fd);
    onUpload();
  };
  return (
    <div className="p-4">
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload} className="bg-green-600 text-white px-4 py-2 ml-2">Upload PDF</button>
    </div>
  );
}
