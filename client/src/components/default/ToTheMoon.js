import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'
import MoonCartoon from '../../images/MoonCartoon.png'
import Container from 'react-bootstrap/Container'

//styles 
import '../../styles/components/default/defaultpage.scss'
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
          <Link className="defaultbuttons" to="/login">
            <Button className="custom-button1" >Login</Button>
          </Link>
          <Link className="defaultbuttons" to="/register">
            <Button className="custom-button2" >Register</Button>
          </Link>
        </div>
      </Container>
    </>
  )



}

export default ToTheMoon