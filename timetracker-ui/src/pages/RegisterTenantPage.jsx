import { useState } from 'react'

// This is page to register new account using email and domain assigned to tenant

function RegisterTenantPage() {

  return (
    <>
    <div>
    <h1>This is page to register new tenant</h1>
      <form>
        <label>Tenant name:</label>
        <input id="tenant"></input>
        <br />

        <label>Tenant code:</label>
        <input id="tenant"></input>
        <br />
        
        <label>Tenant description:</label>
        <input id="tenant"></input>
        <br />
        
        <label>Main country:</label>
        <input id="payment"></input>
        <br />

        <label>Tenant email:</label>
        <input id="email"></input>
        <br />

        <label>Administrator name:</label>
        <input id="email"></input>
        <br />

        <label>Payment option:</label>
        <input id="payment"></input>
        <br />

        <button>Register Tenant</button>

      </form>
      <br />
      <label>New administrative account for given email will be created to manage new Tenant. </label>
      <br />
      <a href="/login">Back to Login page</a>

    </div>
    </>
  )
}

export default RegisterTenantPage
