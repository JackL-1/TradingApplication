import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const LogoutButton = () => {
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  const handleLogout = async () => {
    setIsLoading(true)
    // perform logout actions, e.g. clear user data from local storage, etc.
    // redirect the user to the login page
    navigate('/')
  }

  return (
    <button
      onClick={handleLogout}
      disabled={isLoading}
      className="logoutBtn"
    >
      {isLoading ? (
        'Logging out...'
      ) : null}
    </button>
  )
}

export default LogoutButton

