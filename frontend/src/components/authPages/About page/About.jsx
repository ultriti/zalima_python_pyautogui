import React from 'react';
import Navbar_frame from '../../CommonPages/Navbar_frame';

const About = () => {

  return (
    <div className="bg-blue-500 text-white">
        <div className="navbar_frame h-[8vh] w-full fixed top-0 left-0 bg-amber-500 shadow-md">
        <Navbar_frame />
      </div>

      <div className="container mx-auto py-12 text-center mt-15">
        {/* Hero Section */}
        <h1 className="text-4xl font-bold mb-4">
          POWERFUL WEB SCRAPER FOR REGULAR AND PROFESSIONAL USE
        </h1>
        <p className="text-lg mb-4">
          Automate data extraction in <span className="text-yellow-300">in minutes</span>
        </p>
        <p className="mb-8">
          Extract large amounts of data and easily integrate with other systems.
        </p>
        <div className="flex justify-center gap-4 mb-8">
          <a href="/autoMate">
          <button className="bg-yellow-300 text-black py-2 px-4 rounded hover:bg-yellow-400">
            Start with
          </button>
          </a>
          <button  className="bg-gray-800 cursor-crosshair text-white py-2 px-4 rounded hover:bg-gray-800">
            Install Edge Plugin
          </button>
        </div>
        <p className="text-sm text-gray-300 mb-8">
          FREE scraper for local use • 800,000+ users
        </p>

        {/* Video Section */}
        {/* <div className="mt-8">
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/example_video_id"
            title="Web Scraper Video"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe>
        </div> */}
      </div>

      {/* Feature Section */}
      <div className="bg-white text-black py-12">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Extract data from dynamic websites</h2>
          <p className="mb-4">Point-and-click interface. No coding required.</p>
          <p>Use our FREE Edge plugin for seamless scraping.</p>
        </div>
      </div>
    </div>
  );
};

export default About;
