import { useEffect } from 'react'
import axios from 'axios'

const App = () => {
  useEffect(() => {
    const getData = async () => {
      const { data } = await axios.get('/api/home/') 
      console.log(data)
    }
    getData()
  })

  return <h1>Test! </h1>
}

export default App
