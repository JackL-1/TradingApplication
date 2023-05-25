import React, { useState } from 'react'
import { Modal } from 'react-bootstrap'
import axios from 'axios'

const AddFunds = ({ isOpen, onRequestClose, onSubmit }) => {
  const [amount, setAmount] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()

    try {
      const response = await axios.post('/api/add_funds', {
        amount: amount,
      })

      // Handle the response or perform any necessary actions
      console.log(response.data)

      // Reset the form and close the modal
      setAmount('')
      onRequestClose()
    } catch (error) {
      // Handle any errors that occur during the request
      console.error(error)
    }
  }

  return (
    <Modal isOpen={isOpen} onRequestClose={onRequestClose}>
      <h2>Add Funds</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Amount:
          <input
            type="number"
            value={amount}
            onChange={(event) => setAmount(event.target.value)}
          />
        </label>
        <button type="submit">Add Funds</button>
      </form>
    </Modal>
  )
}

export default AddFunds
