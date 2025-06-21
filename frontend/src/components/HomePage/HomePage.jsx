import React from 'react';
import Navbar_frame from '../CommonPages/Navbar_frame';
import "./homepage.css"
import img1 from "../../../public/images/hp_elem_1.svg"
import img2 from "../../../public/images/hp_elem_2.svg"
import img3 from "../../../public/images/hp_elem_3.svg"

const HomePage = () => {
  return (
    <div className="homepage_frame bg-white min-h-screen flex flex-col w-[100vw]">
      {/* Navbar Section */}
      <div className="navbar_frame h-[8vh] w-full fixed top-0 left-0 bg-amber-500 shadow-md">
        <Navbar_frame />
      </div>

      {/* Main Content */}
      <div className="hp_cont text-center  mt-18 w-ful ">


        <h1 className="text-4xl font-bold text-white mb-4">Welcome to the Home Page</h1>
        <p className="text-lg text-gray-200 mb-6">

          Your one-stop destination to explore and navigate through our features!
        </p>




        {/* Buttons Section */}
        <div className="flex flex-wrap w-[100%] gap-4">
          <div className="homepage_cont min-h-[100vh] w-full ">

            {/* auto mate page 1 */}
            <div className="hp_1 h-[60vh] w-full flex flex-row ">


              <div className="title_cont h-full w-1/2 flex flex-col justify-center ">
                <h1 className="text-blue-400 text-4xl font-bold text-center mb-4">
                  POWERFUL WEB SCRAPER FOR REGULAR AND PROFESSIONAL USE
                </h1>
                {/* Subheading */}
                <p className="text-white text-lg text-center mb-6">
                  Automate data extraction in <span className="text-yellow-300 font-bold">minutes</span>
                </p>
                <a href="/autoMate">
                  <button className="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 shadow-md">
                    Go to scrapping Page
                  </button>
                </a>
              </div>

              <div className="img_div h-[90%] w-1/2 p-10 rounded-3xl overflow-hidden shadow-amber-50">
                <img src={img1} alt="" className='h-full w-full rounded-3xl object-cover ' />
              </div>
            </div>


            {/* ----- about page ----- */}
            <div className="hp_2_cont h-[70vh] w-full flex felx-row ">


              <div className="img_div h-[90%] w-1/2 p-10 rounded-3xl overflow-hidden shadow-amber-50">
                <img src={img2} alt="" className='h-full w-full rounded-3xl object-cover ' />

              </div>

              <div className="title_cont h-full w-1/2 flex flex-col justify-center ">
                <h1 className="text-blue-400 text-4xl font-bold text-center mb-4">
                  visit our about page for more info!
                </h1>
                {/* Subheading */}
                <p className="text-white text-lg text-center mb-6">
                  know more Automate data extraction here <span className="text-yellow-300 font-bold">learn more</span>
                </p>
                <a href="/about">
                  <button className="px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 shadow-md">
                    About Us
                  </button>
                </a>
              </div>
            </div>



            <div className="contact_page_cont h-[70vh] w-full flex flex-row">

              <div className="demo h-full w-1/2 flex flex-col  justify-center">
              <h1 className="text-white text-4xl font-bold text-center mb-4">
                  contact us for more info!
                </h1>
                {/* Subheading */}
                <p className="text-white text-lg text-center mb-6">
                  know more Automate data extraction here <span className="text-yellow-300 font-bold">learn more</span>
                </p>
                <a href="/contact">
                  <button className="px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 shadow-md">
                    Contact Us
                  </button>
                </a>

              </div>
              
              <div className="img_div h-[90%] w-1/2 p-10  rounded-3xl overflow-hidden shadow-amber-50">
                <img src={img3} alt="" className='h-full w-full rounded-3xl object-cover ' />

              </div>
              
              
              

            </div>

            
            {/* contact page ----- */}

          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
