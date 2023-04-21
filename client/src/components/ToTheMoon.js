

//!React
import { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


//! Bootstrap components 
import Container from 'react-bootstrap/Container'
import Mooncartoon from '..images/MoonCartoon.png'




const ToTheMoon = () => {} 
const fetchPrice = async (ticker) => {
  try {
    const response = await fetch('/api/fetch-price/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ticker }),
    })
    const data = await response.json()
    console.log(data.message)
  } catch (error) {
    console.error('Error fetching price:', error)
  }
}

fetchPrice('AAPL')



export default ToTheMoon