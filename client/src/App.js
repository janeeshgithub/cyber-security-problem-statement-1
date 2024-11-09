import React, { useState } from 'react';
import FileUpload from './FileUpload';
import ExtractedText from './ExtractedText';

const App = () => {
  const [extractedText, setExtractedText] = useState('');

  const handleTextExtracted = (text) => {
    setExtractedText(text);
  };

  return (
    <div
      className="relative min-h-screen bg-cover bg-center flex items-center justify-center p-6"
      style={{
        backgroundImage: `url('https://www.supplychainbrain.com/ext/resources/2023/09/11/CYBER-SECURITY-HACKING-iStock-tanawit-sabprasan-1406645290.jpg?t=1694492805&width=1080')`,
      }}
    >
      {/* Dark overlay */}
      <div className="absolute inset-0 bg-black opacity-50"></div>

      {/* Content */}
      <div className="relative z-10 text-center">
        <h1 className="text-3xl font-bold text-white mb-8">File Extractor</h1>
        <FileUpload onTextExtracted={handleTextExtracted} />
        <ExtractedText extractedText={extractedText} />
      </div>
    </div>
  );
};

export default App;
