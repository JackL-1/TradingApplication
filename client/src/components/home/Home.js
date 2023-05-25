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
  const [shouldFetchTradeData, setShouldFetchTradeData] = useState(true)
  const [AddFundsModal, setAddFundsModal] = useState(false)
  const [FundsAmount, setFundsAmount] = useState('')

  // fetches asset data on load 
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

    fetchAssetData()
  }, [])


  // fetches users trades from Database
  // Fetch trade data when shouldFetchTradeData changes
  useEffect(() => {
    const fetchTradeData = async () => {
      try {
        const jwtToken = getToken()
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

    if (shouldFetchTradeData) {
      fetchTradeData()
      setShouldFetchTradeData(false)
    }
  }, [shouldFetchTradeData])

  // Reset shouldFetchTradeData when tradeData changes
  useEffect(() => {
    setShouldFetchTradeData(true)
  }, [])


  // handling the input of funds opens modal 
  const handleAddFundsModal = () => {
    setAddFundsModal(true)
  }

  // closes funds modal 
  const handleCloseFundsModal = () => {
    setAddFundsModal(false)
  }

  const handleSubmitFunds = (amount) => {
    console.log(`Adding funds: $${amount}`)

    setFundsAmount('')
    setAddFundsModal(false)
  }


  const handleLogout = async () => {
    // perform logout actions, e.g. clear user data from local storage
    // redirect the user to the default page
    useNavigate('/')
  }

  return (
    <>
      <div className="hero">
        <h1>ToTheMoon</h1>
        <button className="addFundsBtn" onClick={handleAddFundsModal}>
          Add Funds $
        </button>
        <div className="logoutBtnSurround">
          <LogoutButton onClick={handleLogout} />
        </div>
      </div >
      <div className="timezoneInfo">
        <h2>Please note US Stocks price against NYSE hours: 14:30 - 21:00 GMT+1 </h2>
        <h2>Please note US Stocks price against NYSE hours: 14:30 - 21:00 GMT+1 </h2>
        <h2>Please note US Stocks price against NYSE hours: 14:30 - 21:00 GMT+1 </h2>
        <h2>Please note US Stocks price against NYSE hours: 14:30 - 21:00 GMT+1 </h2>
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