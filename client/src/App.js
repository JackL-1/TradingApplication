import { BrowserRouter, Routes, Route } from 'react-router-dom'


//! Components
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import ToTheMoon from './components/default/ToTheMoon'

const App = () => {

  return (
    <div className="site-wrapper">
      <BrowserRouter>
        <Routes>
          <Route path="/login/" element={<Login />} />
          <Route path="/register/" element={<Register />} />
          <Route path="/" element={<ToTheMoon />} />
        </Routes>
      </BrowserRouter>
    </div>
  )

}

export default App
