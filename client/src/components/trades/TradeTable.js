import React from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/tradetable/tradetable.scss'

const Tradetable = ({ data }) => {
  const minRows = 5
  

  const emptyRows = Math.max(minRows - data.length, 0)
  const rows = data.concat(Array.from({ length: emptyRows }, () => ({ })))

  return (
    <div className='outer-wrapper'>
      <div className='table-wrapper'>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Trade</th>
              <th>Execution Date</th>
              <th>Buy/Sell</th>
              {/* <th>Ticker</th> */}
              <th>Quantity</th>
              <th>Execution Price</th>
              <th>P&amp;L $</th>
            </tr>
          </thead>
          <tbody className='Tablesize'>
            {rows.map((item, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{item && item.execution_timestamp}</td>
                <td className={item && item.buy_sell === 'Buy' ? 'greenbuy' : 'redsell'}>
                  {item && item.buy_sell}
                </td>
                {/* <td>{item && item.Ticker}</td> */}
                <td>{item && item.quantity}</td>
                <td>{item && item.execution_price}</td>
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


