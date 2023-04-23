import React from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/assettable/assettable.scss'

const Assettable = ({ data }) => {
  const minRows = 30

  const emptyRows = Math.max(minRows - data.length, 0)
  const rows = [...data, ...Array(emptyRows).fill(null)]

  return (
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
            {rows.map((item, index) => (
              <tr key={index}>
                <td>{item && item.Ticker}</td>
                <td>{item && item.name}</td>
                <td > product </td>
                <td > Buy </td>
                <td> Sell </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
  )
}

export default Assettable


