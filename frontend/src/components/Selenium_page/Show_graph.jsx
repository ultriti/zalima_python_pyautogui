import React, { useEffect, useState } from "react";
import axios from "axios";

// Import local images
import flipCartHistoryGraph from "../../../public/images/flipCart_history_graph.png";
import flipCartDiscountGraph from "../../../public/images/flipCart_disocunt_graph.png";
import graph from "../../../public/images/graph.png";
import Navbar_frame from "../CommonPages/Navbar_frame";

const ShowGraph = () => {

  const [graphImages, setGraphImages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [getData, setgetData] = useState({})

  const [infoFoundBool, setinfoFoundBool] = useState({})
  const [fileLoc, setfileLoc] = useState('')

  const functionGetGraph = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/filtering",
        { data: "mew" },
        { withCredentials: true }
      );
      console.log(response.status === 200 ? "Filtering done" : "Filtering not done");
    } catch (error) {
      console.error("Error filtering data:", error);
    }
  };

  const getGraphFunction = async () => {
    setLoading(true);
    try {
      const getGraph = await axios.get("http://localhost:8000/api/show-graph", { responseType: "blob" });
      const imageurl = URL.createObjectURL(getGraph.data)

      const images = [
        { src: graph, alt: "Product Analysis Graph" },
        { src: imageurl, alt: "graph" }
      ];

      setGraphImages(images);
    } catch (error) {
      console.error("Error fetching graphs:", error);
    }
    setLoading(false);
  };

  const getFileInfo = async () => {
    try {
      const getGraph = await axios.get("http://localhost:8000/api/get_info", { responseType: "blob" }, { withCredentials: true });

      const getFileLoc = getGraph.data.infoData;
      console.log('-->', getFileLoc);

      setfileLoc(getFileLoc)


    } catch (error) {
      console.error("Error fetching graphs:", error);
    }
    setLoading(false);

  }

  useEffect(() => {
    console.log('-->', location.pathname);
    if (location.pathname == "/show_graph") {
      functionGetGraph();
      getGraphFunction();
    }


  }, []);

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center p-8">
       {/* Navbar Section */}
      <div className="navbar_frame h-[8vh] w-full fixed top-0 left-0 bg-amber-500 shadow-md">
        <Navbar_frame />
      </div>
      <h1 className="text-4xl font-bold text-blue-600 mb-10">Graph Visualization</h1>

      {loading ? (
        <div className="flex flex-col items-center justify-center">
          <svg
            className="animate-spin h-16 w-16 text-blue-600 mb-3"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8h8a8 8 0 01-8 8V4H4z"></path>
          </svg>
          <p className="text-lg text-blue-600 font-medium">Loading graphs...</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full max-w-5xl">
          {graphImages.map((img, index) => (
            <div key={index} className="relative rounded-lg overflow-hidden shadow-md hover:shadow-xl transition duration-300">
              <img src={img.src} alt={img.alt} className="w-full h-auto rounded-lg hover:scale-105 transition duration-300" />
              <p className="text-center text-white bg-gray-800 py-2 absolute bottom-0 w-full opacity-90">{img.alt}</p>
            </div>
          ))}
        </div>
      )}

      <div className="page_2 min-h-[10vh] w-[100%]  mt-10 flex gap-10 items-center">
        <button className="h-20 w-90 bg-amber-400 rounded-2xl cursor-pointer" onClick={() => { getFileInfo() }}>get info</button>

        {
          infoFoundBool ? (
            <a
              href="/text file/info.txt"  // Ensure this matches your public folder structure
              download={fileLoc}
            >
              <button className="h-20 w-90 bg-amber-400 rounded-2xl cursor-pointer">
                Download
              </button>
            </a>
          ) : (<></>)
        }

      </div>


    </div>
  );
};

export default ShowGraph;
