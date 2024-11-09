import React from 'react';

const ExtractedText = ({ extractedText }) => {
  return (
    <div className="p-6 bg-gray-50 rounded-lg shadow-md mt-4">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">Extracted Text</h2>
      <p className="text-gray-700 whitespace-pre-wrap">{extractedText || 'No text extracted yet.'}</p>
    </div>
  );
};

export default ExtractedText;
