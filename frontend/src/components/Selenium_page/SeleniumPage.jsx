import axios from "axios";
import React, { useState } from "react";
import Navbar_frame from "../CommonPages/Navbar_frame";
import { useNavigate } from "react-router-dom";
import "./selenium.css"

const SeleniumInputForm = () => {
    const nav = useNavigate()
    const [website_url, setwebsite_url] = useState('')
    const [custom_parameter, setcustom_parameter] = useState('')
    const [fetched_data, setfetched_data] = useState([])
    const [loading_bool, setloading_bool] = useState(false)


    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");
    const [csvData, setcsvData] = useState('')



    const handleSubmit = async (e) => {
        e.preventDefault();
        setloading_bool(true)
        const send_selenium_data = {
            website_name: website_url,
            custom_parameter: custom_parameter

        }

        console.log(send_selenium_data)

        // You can send the data to a backend server or Python Selenium script here
        const selenium_data = await axios.post("http://localhost:8000/api/selenium_data", send_selenium_data, { withCredentials: true })
            .then((data) => {
                console.log("Success:", data);

                alert("Inputs sent successfully!");
                setloading_bool(false)
                nav("/show_graph")
            })
            .catch((error) => {
                console.error("Error:", error);
                setloading_bool(false)
                alert("Failed to send inputs.");
            });
    };


    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            setStatus("Please select a file first.");
            return;
        }
        const formData = new FormData();
        formData.append("csv", file);
        try {
            const res = await axios.post("http://localhost:8000/api/ml_model", formData, { withCredentials: true });
            if (res.status === 200) {
                alert(res.data.message)
                setcsvData(res.data.fileInfo)
            }else{
                alert(res.data.message)
            }
        } catch (err) {
            alert(err.message)
            console.error(err);
        }
    };


    return (
        <div className="min-h-screen flex flex-col">

            {/* ḥome page 1 */}
            <div className="h-[100vh] w-full flex flex-col items-center justify-center bg-gray-900">
                <div className="navbar_frame h-[8vh] w-full bg-amber-500 fixed top-0 left-0">
                    <Navbar_frame />
                </div>

                <div className="title_selenium h-[4vh] w-full flex flex-row gap-2 items-center justify-center mb-2">
                    <p className="text-gray-300 font-bold text-lg">Scrape any website </p>
                    <p className="text-blue-300 font-bold text-lg"> Here below</p>
                </div>
                <div className="title_seleium h-[5vh] w-full flex flex-row gap-2 items-center justify-center mb-7">
                    <p className="text-gray-300 font-bold text-lg">Upload your</p>
                    <p className="text-blue-300 font-bold text-lg">  csv files</p>
                    <p className="text-gray-300 font-bold text-lg"> below and get your data inforamtion with our ai model</p>
                </div>
                <form
                    className="sele_form bg-white p-6 rounded-lg  max-w-md w-full"
                    onSubmit={handleSubmit}
                >
                    <h2 className="text-2xl font-bold text-gray-300 mb-4 text-center">
                        Selenium Input Form
                    </h2>
                    <div className="mb-4">
                        <label
                            htmlFor="websiteLink"
                            className="block text-gray-200 font-medium mb-2"
                        >
                            Website Link
                        </label>
                        <input
                            type="text"
                            id="websiteLink"
                            name="websiteLink"
                            value={website_url}
                            onChange={(e) => { setwebsite_url(e.target.value) }}
                            placeholder="Enter the website URL"
                            className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring text-white focus:ring-blue-300"
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label
                            htmlFor="customParam"
                            className="block text-gray-200 font-medium mb-2"
                        >
                            Custom Parameter
                        </label>
                        <input
                            type="text"
                            // id="customParam"
                            // name="customParam"
                            value={custom_parameter}
                            onChange={(e) => { setcustom_parameter(e.target.value) }}
                            placeholder="Enter custom input"
                            className="w-full px-3 py-2 border rounded-lg focus:outline-none text-white focus:ring focus:ring-blue-300"
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded-lg transition duration-300"
                    >
                        {
                            loading_bool ? (
                                "Loading..."
                            ) : (
                                "Submit"
                            )
                        }
                    </button>
                </form>
            </div>

            {/* home page 2 */}
            <div className="home_page_2 h-[100vh] flex flex-col items-center justify-center p-10 m-full bg-gray-900">
                <div className="w-full h-full p-6 flex items-center flex-col rounded shadow space-y-4">
                    <h2 className="text-xl font-semibold text-gray-300">Upload CSV Data and get the discount predicted price</h2>
                    <input
                        type="file"
                        accept=".csv"
                        onChange={handleFileChange}
                        className=" w-1/3 text-sm items-center flex justify-center mt-20 bg-gray-500 text-gray-100 border rounded cursor-pointer h-[4vh]"
                    />
                    <button
                        onClick={handleUpload}
                        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                    >
                        Upload
                    </button>
                    {
                        csvData?(
                            <p className="text-2xl text-amber-100">predicted prize data is saved at : {csvData}</p>
                        ):(
                            <></>
                        )
                    }
                </div>
            </div>


        </div>
    );
};

export default SeleniumInputForm;
