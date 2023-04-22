import { BrowserRouter, Routes, Route } from 'react-router-dom'


//! Components
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import ToTheMoon from './components/default/ToTheMoon'
import Home from './components/home/Home'

const App = () => {

  return (
    <div className="site-wrapper">
      <BrowserRouter>
        <Routes>
          <Route path="/login/" element={<Login />} />
          <Route path="/register/" element={<Register />} />
          <Route path="/" element={<ToTheMoon />} />
          <Route path="/home" element={<Home/>} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
