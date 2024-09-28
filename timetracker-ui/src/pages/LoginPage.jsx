import { useState } from 'react'

// This is first page to Log-in to TimeTracker

function LoginPage() {

  return (
    <>
    <div>
    <h1>Login to TimeTracker</h1>
      <form>
        <label>Username:</label>
        <input id="username"></input>
        <br />
        <label>Password:</label>
        <input id="password"></input><br />
        <button>Login</button>
      </form>
      <br />
      <a href="/reset-password">Reset password</a>
      <br />
      <a href="/register-account">Register account</a>
      <br />
      <a href="/register-tenant">Register tenant</a>
    </div>
    </>
  )
}

export default LoginPage
