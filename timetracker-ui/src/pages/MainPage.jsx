import { useState } from 'react'
import { Outlet, Link } from 'react-router-dom'

// Main page with menu, user profile, breadcrumbs, content and footer
// when no token - redirect to /login page
// when incorrect token - redirect to /logout page


function MainPage() {

  const isLogged = true;
  const jwt = "jwt_from_cookie_or_from_Header"
  const account_uid = "johnsmith"
  const account_name = "John"
  const isLoggedOut = false;

  return (
    <>
    <div id="whole-page">
      <div id="top">

        <div id="top-menu">
          <label>Menu:</label> |
          <Link to="/account/list">Accounts</Link> |

          <Link to="/tenant/list">Tenants</Link> | 
          <Link to="/project/list">Projects</Link> |
        </div>

        <div id="top-help">
          <label>Help icon</label>
        </div>

        <div id="top-notification">
          <label>Notification expandable block</label>
        </div>

        <div id="top-user-profile">
          <label>User profile circle</label>
          <Link to="/logout">Logout</Link> |
        </div>

      </div>

      <div id="breadcrumbs">
        <label>Return to Main button | </label>
        <label>Here - You - Are</label>
      </div>

      <div id="middle">
        <Outlet />
      </div>

      <div id="bottom">
        <div id="bottom-footer-centered">
          <label>Copyrights (c) by Someone and Something and whatsoever...</label>
        </div>
      </div>

    </div>

    </>
  )
}

export default MainPage
