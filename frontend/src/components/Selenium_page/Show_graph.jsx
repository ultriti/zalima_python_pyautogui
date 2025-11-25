import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar_frame from "../CommonPages/Navbar_frame";

const ShowGraph = () => {
  const [graphUrl, setGraphUrl] = useState(null);
  const [loading, setLoading] = useState(true);

  const [infoData, setInfoData] = useState(null);
  const [fileUrl, setFileUrl] = useState(null);
  const [infoLoading, setInfoLoading] = useState(false);

  // Helper: format infoData into aligned text
  const formatInfoData = (data) => {
    let output = "";

    const cheapest = data.infoData?.CheapestPrice;
    if (cheapest) {
      output += "=== Cheapest Product ===\n";
      output += `Name: ${cheapest.name}\n`;
      output += `Discount Price: ₹${cheapest.discount_price}\n`;
      output += `Original Price: ₹${cheapest.original_price}\n`;
      output += `Discount Percent: ${cheapest.discount_percent}%\n`;
      output += `Ratings Count: ${cheapest.ratings_count}\n`;
      output += `Reviews Count: ${cheapest.reviews_count}\n`;
      output += `Stars: ${cheapest.reviews_stars}\n\n`;
    }

    const expensive = data.infoData?.MostExpensiveProduct;
    if (expensive) {
      output += "=== Most Expensive Product ===\n";
      output += `Name: ${expensive.name}\n`;
      output += `Discount Price: ₹${expensive.discount_price}\n`;
      output += `Original Price: ₹${expensive.original_price}\n`;
      output += `Discount Percent: ${expensive.discount_percent}%\n`;
      output += `Ratings Count: ${expensive.ratings_count}\n`;
      output += `Reviews Count: ${expensive.reviews_count}\n`;
      output += `Stars: ${expensive.reviews_stars}\n\n`;
    }

    const highestRated = data.infoData?.HighestRatedProduct;
    if (highestRated) {
      output += "=== Highest Rated Product ===\n";
      output += `Name: ${highestRated.name}\n`;
      output += `Discount Price: ₹${highestRated.discount_price}\n`;
      output += `Original Price: ₹${highestRated.original_price}\n`;
      output += `Discount Percent: ${highestRated.discount_percent}%\n`;
      output += `Ratings Count: ${highestRated.ratings_count}\n`;
      output += `Reviews Count: ${highestRated.reviews_count}\n`;
      output += `Stars: ${highestRated.reviews_stars}\n\n`;
    }

    const mostReviewed = data.infoData?.MostReviewedProduct;
    if (mostReviewed) {
      output += "=== Most Reviewed Product ===\n";
      output += `Name: ${mostReviewed.name}\n`;
      output += `Discount Price: ₹${mostReviewed.discount_price}\n`;
      output += `Original Price: ₹${mostReviewed.original_price}\n`;
      output += `Discount Percent: ${mostReviewed.discount_percent}%\n`;
      output += `Ratings Count: ${mostReviewed.ratings_count}\n`;
      output += `Reviews Count: ${mostReviewed.reviews_count}\n`;
      output += `Stars: ${mostReviewed.reviews_stars}\n\n`;
    }

    if (data.infoData?.TopProducts) {
      output += "=== Top Products ===\n";
      data.infoData.TopProducts.forEach((prod, idx) => {
        output += `${idx + 1}. ${prod.name}\n`;
        output += `   Price: ${prod.price || "N/A"}\n`;
        output += `   Reviews: ${prod.reviews || "N/A"}\n`;
        output += `   Rating: ${prod.rating || "N/A"}\n\n`;
      });
    }

    return output;
  };

  // Fetch graph image
  const getGraphFunction = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://localhost:8000/api/show-graph", {
        responseType: "blob",
      });
      const imageUrl = URL.createObjectURL(response.data);
      setGraphUrl(imageUrl);
      console.log('-------------------------------------------');

    } catch (error) {
      console.error("Error fetching graph:", error);
    }
    setLoading(false);
  };

  // Fetch info data
  const handleGetInfo = async (e) => {
    // e.pventDefault()
    setInfoLoading(true);
    try {
      const res = await axios.get("http://localhost:8000/api/get_info", {
        withCredentials: true,
      });

      if (res.status === 200) {
        const data = res.data; // axios already gives parsed JSON
        // console.log("infoData", data);

        // setInfoData(data);

        // Save to localStorage
        // localStorage.setItem("data_selenium", JSON.stringify(data));

        // Format and create TXT blob
        // const formattedText = formatInfoData(data);
        // const blob = new Blob([formattedText], { type: "text/plain" });
        // const downloadUrl = URL.createObjectURL(blob);
        // setFileUrl(downloadUrl);
        console.log('-------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>');
        
      } else {
        
        console.log("error");
      }
    } catch (err) {
      console.error("Error fetching info:", err);
      alert("Failed to fetch info.");
    }
  };

  // Restore from localStorage on reload
  useEffect(() => {
    if (location.pathname === "/show_graph") {
      getGraphFunction();
    }

    // const stored = localStorage.getItem("data_selenium");
    // if (stored) {
    //   try {
    //     const parsed = JSON.parse(stored);
    //     setInfoData(parsed);

    //     const formattedText = formatInfoData(parsed);
    //     const blob = new Blob([formattedText], { type: "text/plain" });
    //     const downloadUrl = URL.createObjectURL(blob);
    //     setFileUrl(downloadUrl);
    //   } catch (err) {
    //     console.error("Failed to parse stored data:", err);
    //   }
    // }
    console.log('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>');
  }, []);

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center p-8">
      {/* Navbar Section */}
      {/* <div className="navbar_frame h-[8vh] w-full fixed top-0 left-0 bg-amber-500 shadow-md">
        <Navbar_frame />
      </div> */}

      <h1 className="text-4xl font-bold text-blue-600 mb-10">Graph Visualization</h1>

      {/* Graph Section */}
      {loading ? (
        <div className="flex flex-col items-center justify-center">
          <p className="text-lg text-blue-600 font-medium">Loading graph...</p>
        </div>
      ) : (
        graphUrl ? (
          <div className="relative rounded-lg overflow-hidden shadow-md hover:shadow-xl transition duration-300">
            <img
              src={graphUrl}
              alt="Graph from backend"
              className="w-full h-auto rounded-lg hover:scale-105 transition duration-300"
            />
            <p className="text-center text-white bg-gray-800 py-2 absolute bottom-0 w-full opacity-90">
              Graph from backend
            </p>
          </div>
        ) : (
          <>
          </>
        )
      )}

      {/* Info Section */}
      <div className="page_2 min-h-[10vh] w-full mt-10 flex flex-col items-center gap-6">
        <button
          className="h-12 px-6 bg-amber-400 rounded-2xl cursor-pointer font-bold hover:bg-amber-500"
          onClick={() => { handleGetInfo() }}
        >
          {infoLoading ? "Fetching Info..." : "Get Info"}
        </button>

        {infoData && (
          <div className="bg-white shadow-md rounded-lg p-4 w-full max-w-3xl">
            <h2 className="text-xl font-semibold text-blue-600 mb-2">Info Data</h2>
            <pre className="bg-gray-100 p-3 rounded-md text-sm overflow-x-auto">
              {formatInfoData(infoData)}
            </pre>

            {fileUrl && (
              <a href={fileUrl} download="infoData.txt" onClick={(e) => e.stopPropagation()}>
                <button>Download Info File</button>
              </a>

            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default ShowGraph;
