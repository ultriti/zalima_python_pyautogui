import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import './App.css'
import PageNotFound from './components/CommonPages/PageNotFound'
import HomePage from './components/HomePage/HomePage'
import Register_page from './components/authPages/Register_page'
import LoginPage from './components/authPages/LoginPage'
import LogoutPage from './components/authPages/LogoutPage'
import SeleniumInputForm from './components/Selenium_page/SeleniumPage'
import Show_graph from './components/Selenium_page/show_graph'
import About from './components/authPages/About page/About'
import Contact_page from './components/authPages/About page/Contact_page'
import Ai_Model from './components/machineLearning-Pages/Ai_Model'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<About />} />
          <Route path="/autoMate" element={<SeleniumInputForm />} /> 
          <Route path="/contact" element={<Contact_page />} /> 
          <Route path="/show_graph" element={<Show_graph />} />

          {/* ai model */}
          <Route path="/ai_model" element={<Ai_Model />} />
          
          {/* auth routes */}
          <Route path="/user/register" element={<Register_page/>} />
          <Route path="/user/login" element={<LoginPage />} />
          <Route path="/user/logout" element={<LogoutPage />} />

          {/* page not found route */}
          <Route path="*" element={<PageNotFound />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
