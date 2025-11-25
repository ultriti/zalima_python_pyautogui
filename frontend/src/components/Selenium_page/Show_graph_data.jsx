import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar_frame from "../CommonPages/Navbar_frame";
import "./Show_graph_.css"
import txt from "../../../public/text file/info.txt"

const Show_graph_data = () => {

    const [graphUrl, setGraphUrl] = useState(null);
    const [loading, setLoading] = useState(true);

    const [infoData, setInfoData] = useState(null);
    const [fileUrl, setFileUrl] = useState("frontend\public\text file\info.txt");
    const [infoLoading, setInfoLoading] = useState(false);


    const getGraphFunction = async () => {
        setLoading(true);
        const data = {
            data : "ehllo"
        }
        try {
            const response_filter = await axios.post("http://localhost:8000/api/filtering",data, {
                withCredentials: true
            });
            if (response_filter.status == 200) {
                const response = await axios.get("http://localhost:8000/api/show-graph", {
                    responseType: "blob",
                });
                const imageUrl = URL.createObjectURL(response.data);
                setGraphUrl(imageUrl);
                console.log('-------------------------------------------');

            }

        } catch (error) {
            console.error("Error fetching graph:", error);
        }
        setLoading(false);
    };

    const get_info_axios = async () => {
        const response = await axios.get("http://localhost:8000/api/get_info", {
            withCredentials: true,
        });

        if (response.status == 200) {
            console.log('txt', response.data);

            localStorage.removeItem("data_selenium")
            localStorage.setItem("data_selenium", response.data)
            const local_data = localStorage.getItem("data_selenium");
            setInfoData(local_data)
        }
    }

    useEffect(() => {
        getGraphFunction()

    }, [])




    return (
        <div className="bg_show_graph">

            <div className="bg_show_cont">

                <div className="img_grpah_div">
                    {
                        graphUrl ? (
                            <img src={graphUrl} alt="" />
                        ) : (
                            <></>
                        )
                    }
                </div>

                <div className="getDetail_frame">

                    <div className="getDetail_frame_cont">
                        <button className="btn_getinfo" onClick={() => { get_info_axios() }}>get info</button>
                        {
                            infoData ? (
                                <>
                                    {txt && (
                                        <a href={txt} download="infoData.txt" onClick={(e) => e.stopPropagation()}>
                                            <button className="down_file_btn">Download Info File</button>
                                        </a>

                                    )}
                                </>
                            ) : (
                                <></>
                            )
                        }
                        <div className="getinfo_data_display">
                            {
                                infoData ? (
                                    <p>{infoData}</p>
                                ) : (
                                    <></>
                                )
                            }

                        </div>






                    </div>

                </div>

            </div>

        </div>
    )
}

export default Show_graph_data
