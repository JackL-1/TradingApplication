import React from 'react'
import Tradetable from '../trades/TradeTable'
import Assettable from '../assets/AssetTable'
import axios from 'axios'
import { useState, useEffect } from 'react'


//styles 
import '../../styles/components/home/home.scss'

const Home = () => {
  const [data, setData] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://localhost:8000/api/assets/')

      const Assets = response.data
      console.log('DATA:', Assets)
      console.log('Name:', Assets.AssetData[0].name)
      console.log('Ticker:', Assets.AssetData[0].ticker)
      console.log('product:', Assets.AssetData[0].product)


      setData(Assets.AssetData)
    }

    fetchData()
  }, [])

  return (
    <>
      <section className='background'>
        <div className="tradetabledefaultpage" >

          <Assettable data={data} />
        </div>
        <div className="assettabledefaultpage" >
          {/* <Tradetable data={data} /> */}
        </div>
      </section>
    </>
  )
}

export default Home