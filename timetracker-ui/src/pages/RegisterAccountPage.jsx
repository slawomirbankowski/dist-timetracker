import { useState } from 'react'

// This is page to register new account using email and domain assigned to tenant

function RegisterAccountPage() {

  return (
    <>
    <div>
    <h1>This is page to register new account</h1>
      <form>
        <label>Tenant:</label>
        <input id="tenant"></input>
        <br />

        <label>Username:</label>
        <input id="username"></input>
        <br />

        <label>Email:</label>
        <input id="email"></input><br />

        <label>PIN:</label>
        <input type="secret" id="pin"></input><br />

        <label>Birth date:</label>
        <input id="birth_date"></input><br />

        <button>Register Account</button>

      </form>
      <a href="/login">Back to Login page</a>
    </div>
    </>
  )
}

export default RegisterAccountPage
