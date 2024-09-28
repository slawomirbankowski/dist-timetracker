import { useState } from 'react'

// This is page to register new account using email and domain assigned to tenant

function ResetPasswordPage() {

  return (
    <>
    <div>
    <h1>This is page to reset password for existing user</h1>
      <form>

        <label>Email:</label>
        <input id="email"></input>
        <br />

        <label>PIN:</label>
        <input id="pin"></input><br />

        <label>Birth date:</label>
        <input id="birth_date"></input><br />

        <button>Send link to reset password</button>

      </form>
      <br />
      <a href="/login">Back to Login page</a>
    </div>
    </>
  )
}

export default ResetPasswordPage
