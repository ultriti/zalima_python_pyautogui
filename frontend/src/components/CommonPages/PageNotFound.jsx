import React from "react";
import { Link } from "react-router-dom";

const PageNotFound = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-9xl font-extrabold text-gray-800">404</h1>
      <h2 className="text-4xl font-bold text-gray-600 mt-4">
        Page Not Found
      </h2>
      <p className="text-lg text-gray-500 mt-2">
        Sorry, the page you're looking for doesn't exist.
      </p>
      <Link
        to="/"
        className="mt-6 px-6 py-3 bg-blue-600 text-white text-lg font-medium rounded hover:bg-blue-700 transition"
      >
        Back to Home
      </Link>
    </div>
  );
};

export default PageNotFound;
