import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

// Bootstrap
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

//Styles 
import '../../styles/auth/login.scss'


const Login = () => {

  // ! Location variables
  const navigate = useNavigate()

  // ! State
  const [formFields, setFormFields] = useState({
    email: '',
    password: '',
  })
  const [error, setError] = useState('')

  // ! Executions
  const handleChange = (e) => {
    setFormFields({ ...formFields, [e.target.name]: e.target.value })
    setError('')
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log('formFields:', formFields)
    try {
      const { data } = await axios.post('api/auth/login/', formFields)
      
      localStorage.setItem('MoonToken', data.token)
      console.log('DATA TOKEN', data.token)
      axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`
      navigate('/home')
    } catch (err) {
      console.log('error', err)
      setError(err.response.data.message)
    }
  }

  return (
    <main className="loginpage">
      <Container className='loginbg'>
        <Row>
          <Col className ='loginpage' as="form" xs={{ span: 10, offset: 1 }} sm={{ span: 8, offset: 2 }} md={{ span: 6, offset: 3 }} onSubmit={handleSubmit}>
            <h1 className='logintitle'>Login</h1>
            <label htmlFor="email"> Email</label>
            <input type="text" name="email" placeholder=' Email' onChange={handleChange} value={formFields.email} />
            <label htmlFor="password">Password</label>
            <input type="password" name="password" placeholder='Password' onChange={handleChange} value={formFields.password} />
            <div className='btnCenter'>
              <button className='btn mb-4'>Login</button>
            </div>
            {error && <p className='text-danger text-center'>{error}</p>}
          </Col>
        </Row>
      </Container>
    </main>
  )
}

export default Login




