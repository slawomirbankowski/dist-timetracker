import { useState } from 'react'

// Page to Log-out from TimeTracker and safely deactivate token
// after a while redirect to /login page

function LogoutPage() {

  return (
    <>
    <div>
      <h1>User has been logged out</h1>
      <a href="/login">Back to login page</a>
    </div>
    </>
  )
}

export default LogoutPage
