import React from 'react';
import axios from 'axios';

const LogoutButton = () => {
  const handleLogout = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/logout', {}, { withCredentials: true });
      alert(response.data.message);
      window.location.href = '/user/login';
    } catch (error) {
      alert('Logout failed. Please try again.');
    }
  };

  return (
    <button
      onClick={handleLogout}
      className="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded transition duration-300"
    >
      Log Out
    </button>
  );
};

export default LogoutButton;
