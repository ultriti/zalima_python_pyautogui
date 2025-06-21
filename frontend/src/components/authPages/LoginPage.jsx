import React, { useState } from "react";
import "./LoginPage.css"
import { useNavigate } from "react-router-dom"
import axios from "axios";
import Navbar_frame from "../CommonPages/Navbar_frame";

const LoginPage = () => {
  const nav = useNavigate()
  const [email, setemail] = useState('')
  const [password, setpassword] = useState('')

  const handleLogin = async (e) => {
    e.preventDefault()
    const send_login_data = {
      email: email,
      password: password,

    }
    const send_login_data_axios = await axios.post(`${import.meta.env.VITE_BASE_URL}/api/user/login`, send_login_data, { withCredentials: true })
    if (send_login_data_axios.status === 200) {
      alert(send_login_data_axios.data.message)
      nav("/")
    } else {
      alert(send_login_data_axios.data.error)
    }
  }

  return (
    <div className="login_page_frame min-h-screen flex flex-col align-center justify-center items-center  bg-gradient-to-r from-green-500 to-blue-500">
      
      <div className="navbar_frame h-[8vh] w-full bg-amber-500 fixed top-0 left-0">
        <Navbar_frame/>
      </div>
      
      <div className="RegisterPage_form  bg-white p-8 rounded-lg shadow-lg w-96">
        <div className="flex justify-center mb-4">
          <div className="bg-gray-200 p-4 rounded-full">
            <i className="fas fa-lock text-gray-600 text-2xl"></i>
          </div>
        </div>
        <h2 className="text-2xl font-bold text-center mb-6">Login</h2>
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => { setemail(e.target.value) }}
              className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => { setpassword(e.target.value) }}
              className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your password"
            />
          </div>
          <div className="flex items-center justify-between mb-4">
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" />
              Remember me
            </label>
            <a href="#" className="text-blue-500 hover:underline">
              Forgot Password?
            </a>
          </div>
          <button
            type="submit"
            className="w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
          >
            Login
          </button>
        </form>
        <div className="text-center mt-4">
          <p>
            Don't have an account?{" "}
            <a href="/user/register" className="text-blue-500 hover:underline">
              Register here
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
