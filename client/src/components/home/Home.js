import React from 'react'
import axios from 'axios'
import Tradetable from '../trades/TradeTable'
import Assettable from '../assets/AssetTable'

import { getPayload, isAuthenticated, removeToken, getToken, authenticated } from '../auth/helpers/auth'

import { useState, useEffect, useCallback } from 'react'

import LogoutButton from '../auth/logout'
import AddFunds from './addfunds'

//styles 
import '../../styles/components/home/home.scss'
import { useNavigate } from 'react-router-dom'

const Home = () => {
  const [assetData, setAssetData] = useState(null)
  const [tradeData, setTradeData] = useState([])

  // const [isModalOpen, setIsModalOpen] = useState(false)

  // const handleAddFunds = async (amount) => {
  //   try {
  //     const response = await axios.post('/api/add_funds', {
  //       amount: amount,
  //     })
  //     console.log(response.data)
  //   } catch (error) {
  //     console.error(error)
  //   }
  //   setIsModalOpen(false)
  // }



  useEffect(() => {
    const fetchAssetData = async () => {
      try {
        const jwtToken = getToken() // Retrieve the JWT token from local storage
        const response = await authenticated.get('/api/assets/', {
          headers: {
            Authorization: `Bearer ${jwtToken}`,
          },
        })
  
        const assets = response.data
        setAssetData(assets.AssetData)
  
        console.log('ASSETDATA:', assets)
      } catch (error) {
        console.error('Error fetching asset data:', error)
      }
    }
  
    const fetchTradeData = async () => {
      try {
        const jwtToken = getToken() // Retrieve the JWT token from local storage
        const response = await authenticated.get('/api/trades/', {
          headers: {
            Authorization: `Bearer ${jwtToken}`,
          },
        })
  
        const trades = response.data
        setTradeData(trades.TradeData)
  
        console.log('TRADEDATA:', trades.TradeData)
        console.log('Execution_Price:', trades.TradeData[0].execution_price)
      } catch (error) {
        console.error('Error fetching trade data:', error)
      }
    }
  
    fetchTradeData()
    fetchAssetData()
  }, [tradeData])
  


  const handleLogout = async () => {
    // perform logout actions, e.g. clear user data from local storage
    // redirect the user to the default page
    useNavigate('/')
  }

  return (
    <>
      <div className="hero">
        <h1>ToTheMoon</h1>
        {/* <AddFunds className='addfunds' onClick={handleAddFunds} /> */}
        <LogoutButton className='logout' onClick={handleLogout} />
      </div>
      <section className='background'>
        <div className="assettabledefaultpage" >

          <Assettable data={assetData} />
        </div>
        <div className="tradetabledefaultpage" >
          <Tradetable data={tradeData} />
        </div>
      </section>
    </>
  )
}

export default Home