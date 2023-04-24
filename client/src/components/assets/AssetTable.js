import React, { useState } from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/assettable/assettable.scss'
import axios from 'axios'

const AssetTable = ({ data }) => {
  const [searchQuery, setSearchQuery] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [selectedAsset, setSelectedAsset] = useState({})
  const [quantity, setQuantity] = useState(0)
  const [action, setAction] = useState('')

  if (!data) {
    return <div>Loading...</div>
  }

  const filteredData = data.filter((item) =>
    item.name.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const handleBuyClick = (asset) => {
    setSelectedAsset(asset)
    setAction('Buy')
    setShowModal(true)
  }

  const handleSellClick = (asset) => {
    setSelectedAsset(asset)
    setAction('Sell')
    setShowModal(true)
  }


  const handleSubmit = async (event) => {
    event.preventDefault()
  
    if (!['Buy', 'Sell'].includes(action)) {
      alert('Please select either Buy or Sell')
      return
    }
  
    try {
      const response = await axios.post('http://localhost:8000/api/pre_confirm/', {
        ticker: selectedAsset.ticker,
        buy_sell: action,
        quantity: quantity,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
  
      console.log(response.data)
  
      const tradeResponse = await axios.post('http://localhost:8000/api/trade/', {
        ticker: response.data.ticker,
        buy_sell: action,
        quantity: response.data.quantity,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
  
      console.log(tradeResponse.data)
      setShowModal(false)
    } catch (error) {
      console.error(error)
    }
  }
  
 

  return (
    <div className="outer-wrapper">
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search by name..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>
      <div className="outer-wrapper">
        <div className="table-wrapper">
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Ticker</th>
                <th>Name</th>
                <th>Product</th>
                <th>Buy</th>
                <th>Sell</th>
              </tr>
            </thead>
            <tbody className="Tablesize">
              {Array.isArray(filteredData) &&
                filteredData.map((item) => (
                  <tr key={item.id}>
                    <td>{item.ticker}</td>
                    <td>{item.name}</td>
                    <td>{item.product}</td>
                    <td>
                      <button className='buybutton' onClick={() => handleBuyClick(item)}>Buy</button>
                    </td>
                    <td>
                      <button className='sellbutton' onClick={() => handleSellClick(item)}>Sell</button>
                    </td>
                  </tr>
                ))}
            </tbody>
          </Table>
        </div>
      </div>
      {showModal && (
        <div className="modal">
          <form className="modal-content" onSubmit={handleSubmit}>
            <p>{selectedAsset.name}</p>
            <p>{selectedAsset.ticker}</p>
            <label>
              Quantity:
              <input
                type="number"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
                min={0}
              />
            </label>
            <label>
              Buy/Sell:
              <select value={action} onChange={(e) => setAction(e.target.value)}>
                <option value="Buy">Buy</option>
                <option value="Sell">Sell</option>
              </select>
            </label>
            <button type="submit">Submit</button>
            <button type="button" onClick={() => setShowModal(false)}>Close</button>
          </form>
        </div>
      )}
    </div>
  )
}
export default AssetTable
