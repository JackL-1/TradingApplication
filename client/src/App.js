import { BrowserRouter, Routes, Route } from 'react-router-dom'


import { useEffect } from 'react'
import axios from 'axios'

const App = () => {

  return (
    <div className="site-wrapper">
      <BrowserRouter>
        <Routes>
          {/* <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} /> */}
        </Routes>
      </BrowserRouter>
    </div>
  )

}

export default App
