import axios from "axios";
import React, { useState } from "react";

const Ai_Model = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [labels, setLabels] = useState([]);  // Array to store multiple labels
  const [value_col, setvalue_col] = useState('')
  const [inputValue, setInputValue] = useState(""); // Single input value
  const [inputValue2, setInputValue2] = useState(""); // Second input value

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (!file) {
      alert("Please select a file to upload.");
      return;
    }
    setSelectedFile(file);
  };

  const handleLabelChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleLabelChange2 = (event) => {
    setInputValue2(event.target.value);
  };

  // Add label to array when user presses "Enter"
  const handleKeyPress = (event) => {
    if (event.key === "Enter" && inputValue.trim()) {
      setLabels([...labels, inputValue.trim()]);
      setInputValue(""); // Clear input field
    }
  };

  const handleKeyPress2 = (event) => {
    if (event.key === "Enter" && inputValue2.trim()) {
      setLabels([...labels, inputValue2.trim()]);
      setInputValue2(""); // Clear input field
    }
  };

  const sendFile = async () => {
    if (!selectedFile) {
      alert("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("labels", JSON.stringify(inputValue)); // Send array as JSON string
    formData.append("value_col", JSON.stringify(inputValue2)); // Send array as JSON string

    console.log('formdata',formData);
    

    try {
      const response = await fetch(`${import.meta.env.VITE_BASE_URL}/api/ml-model`, {
        method: "POST",
        body: formData,
      });

      const result = await response.json();
      alert(result.message);
      predict_values();
    } catch (error) {
      console.error("Error uploading the file:", error);
    }
  };

  // const predict_values = async () => {
  //   try {
  //     const response = await axios.get(`${import.meta.env.VITE_BASE_URL}/api/ml-model/predict`, { withcredentials: true });

  //     if (response.status === 200) {
  //       const result = await response.data;
  //       console.log("Predicted values:", result);
  //     }else{
  //       alert(response.data.message)
  //     }

  //   } catch (error) {
  //     console.error("Error predicting values:", error);

  //   }
  // }


  return (
    <div className="items-center justify-center min-h-screen bg-gray-800 flex flex-col p-60">
      <div className="bg-white rounded-lg shadow-md text-center flex flex-col gap-5 w-[50vw] px-50 py-6">
        <h1 className="text-xl font-bold mb-4">Upload Your File & Labels</h1>

        {/* File Upload Input */}
        <label className="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Select File
          <input type="file" hidden onChange={handleFileUpload} />
        </label>

        {selectedFile && <p className="mt-3 text-gray-700">Selected file: {selectedFile.name}</p>}

        {/* Labels Input */}
        <input
          type="text"
          placeholder="Enter label value & press Enter"
          value={inputValue}
          onChange={handleLabelChange}
          onKeyPress={handleKeyPress}
          className="border p-2 rounded w-full"
        />

        {/* Second Label Input */}
        <input
          type="text"
          placeholder="Enter second label value & press Enter"
          value={inputValue2}
          onChange={handleLabelChange2}
          onKeyPress={handleKeyPress2}
          className="border p-2 rounded w-full"
        />

        {/* Display Added Labels */}
        <div className="mt-3 flex flex-wrap gap-2">
          {labels.map((label, index) => (
            <span key={index} className="bg-gray-200 px-3 py-1 rounded">{label}</span>
          ))}
        </div>

        <button onClick={sendFile} className="bg-green-500 text-white px-4 py-2 rounded mt-3 hover:bg-green-600">
          Upload File & Labels
        </button>
      </div>
    </div>
  );
};

export default Ai_Model;