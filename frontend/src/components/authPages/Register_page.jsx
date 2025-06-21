import React, { useState } from "react";
import "./RegisterPage.css"
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Navbar_frame from "../CommonPages/Navbar_frame";

const RegisterPage = () => {
  const nav = useNavigate()
  const [username, setusername] = useState('')
  const [email, setemail] = useState('')
  const [password, setpassword] = useState('')

  const handleRegister = async (e) => {
    e.preventDefault()
    const send_login_data = {
      name: username,
      email: email,
      password: password,
    }
    const send_login_data_axios = await axios.post(`${import.meta.env.VITE_BASE_URL}/api/user/register`, send_login_data, { withCredentials: true })

    if (send_login_data_axios.status === 201) {
      alert(send_login_data_axios.data.message)
      nav("/")
    } else {
      alert(send_login_data_axios.error)
    }
  }



  return (
    <div className="RegisterPage_frame min-h-screen flex items-center justify-center bg-gradient-to-r from-pink-500 to-blue-500">
      <div className="navbar_frame h-[8vh] w-full bg-amber-500 fixed top-0 left-0">
        <Navbar_frame/>
      </div>
      <div className="RegisterPage_form p-8 rounded-[20px] shadow-lg w-96">
        <div className="flex justify-center mb-4">
          <div className="bg-gray-200 p-4 rounded-full">
            <i className="fas fa-user text-gray-200 text-2xl"></i>
          </div>
        </div>
        <h2 className="text-2xl font-bold text-center mb-6">Register</h2>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label className="block text-gray-900 font-[700]">username</label>
            <input
              type="username"
              value={username}
              onChange={(e) => { setusername(e.target.value) }}
              className="username w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your username"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-900 font-[700]">email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => { setemail(e.target.value) }}
              className="email w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-900 font-[700]">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => { setpassword(e.target.value) }}
              className="password w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
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
            className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600"
          >
            Register
          </button>
          <div className="text-center mt-4">
            <p>
              already have an account?{" "}
              <a href="/user/login" className="text-blue-500 hover:underline">
                login here
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default RegisterPage;
