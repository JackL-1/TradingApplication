import React from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/tradetable/tradetable.scss'

const Tradetable = ({ data }) => {
  const minRows = 30
  const ROW_HEIGHT = 45

  const emptyRows = Math.max(minRows - data.length, 0)
  const rows = [...data, ...Array(emptyRows).fill(null)]

  return (
    <div className='outer-wrapper'>
      <div className='table-wrapper'>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Trade</th>
              <th>Execution Date</th>
              <th>Buy/Sell</th>
              <th>Ticker</th>
              <th>Quantity</th>
              <th>Execution Price</th>
              <th>P&L</th>
            </tr>
          </thead>
          <tbody className='Tablesize'>
            {rows.map((item, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{item && item.ExecutionDate}</td>
                <td className={item && item.buysell === 'Buy' ? 'greenbuy' : 'redsell'}>
                  {item && item.buysell}
                </td>
                <td>{item && item.Ticker}</td>
                <td>{item && item.Quantity}</td>
                <td>{item && item.ExecutionPrice}</td>
                <td className={item && item.pnl >= 0 ? 'greenbuy' : 'redsell'}>
                  {item && item.pnl}
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
  )
}

export default Tradetable


