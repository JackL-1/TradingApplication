import React from 'react'
import Tradetable from '../trades/TradeTable'

//styles 
import '../../styles/components/home/home.scss'



const Home = () => {
  const data = [
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Sell', pnl: 2.86 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: -3.874 },
    { Ticker: 'AAPL', Quantity: '5.00', ExecutionPrice: '@166.75', ExecutionDate: '2023-04-21 13:10:43.78', buysell: 'Buy', pnl: 5.372 }
    
  ]
  return (
    <>
      <section className='background'>
        <div className="TradeTable" style={{ height: '100px' }}> 
          <Tradetable data={data} />
        </div>
      </section>
    </>
  )
}

export default Home