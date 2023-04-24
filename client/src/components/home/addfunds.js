// import React, { useState } from 'react'
// import Modal from 'react-modal'

// const AddFunds = ({ isOpen, onRequestClose, onSubmit }) => {
//   const [amount, setAmount] = useState('')

//   const handleSubmit = (event) => {
//     event.preventDefault()
//     onSubmit(amount)
//   }

//   return (
//     <Modal isOpen={isOpen} onRequestClose={onRequestClose}>
//       <h2>Add Funds</h2>
//       <form onSubmit={handleSubmit}>
//         <label>
//           Amount:
//           <input
//             type="number"
//             value={amount}
//             onChange={(event) => setAmount(event.target.value)}
//           />
//         </label>
//         <button type="submit">Add Funds</button>
//       </form>
//     </Modal>
//   )
// }

// export default AddFunds
