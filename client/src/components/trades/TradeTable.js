import React from 'react'
import Table from 'react-bootstrap/Table'
import '../../styles/components/tradetable/tradetable.scss'

const Tradetable = ({ data }) => {
  return (
    <>
      <div className='outer-wrapper'>
        <div className='table-wrapper'>
          <table>
            <thead>
              <th>Trade</th>
              <th>Execution Date</th>
              <th>Buy/Sell</th>
              <th>Ticker</th>
              <th>Quantity</th>
              <th>Execution Price</th>
              <th>P&L</th>

            </thead>
            <tbody className='Tablesize'>
              {data.map((item, index) => (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{item.ExecutionDate}</td>
                  <td className={item.buysell === 'Buy' ? 'greenbuy' : 'redsell'}>
                    {item.buysell}
                  </td>
                  <td>{item.Ticker}</td>
                  <td>{item.Quantity}</td>
                  <td>{item.ExecutionPrice}</td>
                  <td className={item.pnl >= 0 ? 'greenbuy' : 'redsell'}>
                    {item.pnl}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  )
}

export default Tradetable

