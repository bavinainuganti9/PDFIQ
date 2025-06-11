import React, { useState } from "react";
import Uploader from "./components/Uploader";
import QAInterface from "./components/QAInterface";

export default function App() {
  const [uploaded, setUploaded] = useState(false);
  return (
    <div className="max-w-3xl mx-auto py-6">
      <h1 className="text-2xl font-bold mb-4">PDFIQ – Semantic Q&A</h1>
      <Uploader onUpload={() => setUploaded(true)} />
      {uploaded && <QAInterface />}
    </div>
  );
}
