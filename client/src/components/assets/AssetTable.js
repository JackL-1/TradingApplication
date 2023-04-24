import React from 'react'
import { useState, useEffect } from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/assettable/assettable.scss'

const Assettable = ({ data }) => {
  const [searchQuery, setSearchQuery] = useState('')

  if (!data) {
    return <div>Loading...</div>
  }

  const filteredData = data.filter(item => {
    return item.name.toLowerCase().includes(searchQuery.toLowerCase())
  })

  return (
    <div className='outer-wrapper'>
      <div className='search-bar'>
        <input type='text' placeholder='Search by name...' value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
      </div>
      <div className='outer-wrapper'>
        <div className='table-wrapper'>
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
            <tbody className='Tablesize'>
              {Array.isArray(filteredData) && filteredData.map((item) => (
                <tr key={item.id}>
                  <td>{item.ticker}</td>
                  <td>{item.name}</td>
                  <td>{item.product}</td>
                  <td>Buy</td>
                  <td>Sell</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </div>
      </div>
    </div>
  )
}


export default Assettable