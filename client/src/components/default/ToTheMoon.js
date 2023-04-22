import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'
import MoonCartoon from '../../images/MoonCartoon.png'
import Container from 'react-bootstrap/Container'
import '../../styles/default/defaultpage.scss'
import candlesticks from '../../images/candlesticks.png'


const ToTheMoon = () => {
  return (
    <>
      <Container className="bg_container">
        <div className="content-wrapper">
          <section>
            <div className="moon"></div>
          </section>
        </div>
        <h1>
          <span>
            <span className='green'>T</span>
            <span className='red'>0</span>
            <span className='green'> </span>
            <span className='green'>T</span>
            <span className='red'>H</span>
            <span className='green'>E</span>

            <img className='candlesticks' src={candlesticks} />
          </span>
          <span>MooN</span>
        </h1>

        <div className="button-container">
          <Link to="/login">
            <Button variant="primary">Login</Button>
          </Link>
          <Link to="/register">
            <Button variant="secondary">Register</Button>
          </Link>
        </div>
      </Container>
    </>
  )



}

export default ToTheMoon