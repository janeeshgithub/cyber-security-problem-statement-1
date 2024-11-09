import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ onTextExtracted }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    formData.append('apikey', '77f73a48d688957');
    formData.append('language', 'eng');

    setLoading(true);
    try {
      const response = await axios.post('https://api.ocr.space/parse/image', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      const extractedText = response.data.ParsedResults[0].ParsedText;
      onTextExtracted(extractedText);
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Failed to extract text. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 bg-gray-300 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">Upload File</h2>
      <div className="flex flex-col items-center space-y-4">
        <input
          type="file"
          onChange={handleChange}
          className="block w-full text-sm text-green-950
                     file:mr-4 file:py-2 file:px-4
                     file:rounded-full file:border-0
                     file:text-sm file:font-semibold
                     file:bg-grey-50 file:text-blue-700
                     hover:file:bg-blue-100"
        />
        <button
          onClick={handleSubmit}
          className="bg-green-600 text-white font-medium py-2 px-6 rounded-lg hover:bg-green-950 transition duration-200"
          disabled={loading}
        >
          {loading ? 'Extracting...' : 'Upload File'}
        </button>
      </div>
    </div>
  );
};

export default FileUpload;
