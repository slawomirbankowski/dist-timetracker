import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css'

import MainPage from './pages/MainPage.jsx'
import LoginPage from './pages/LoginPage.jsx'
import LogoutPage from './pages/LogoutPage.jsx'
import RegisterAccountPage from './pages/RegisterAccountPage.jsx'
import RegisterTenantPage from './pages/RegisterTenantPage.jsx'
import ResetPasswordPage from './pages/ResetPasswordPage.jsx'
import HelpPage from './pages/HelpPage.jsx'
import LicensePage from './pages/LicensePage.jsx'
import ErrorPage from './pages/ErrorPage.jsx'
import NotFoundPage from './pages/NotFoundPage.jsx'

import UnfinishedOutlet from './pages/outlets/UnfinishedOutlet.jsx'
import AccountListOutlet from './pages/outlets/AccountListOutlet.jsx'
import TenantListOutlet from './pages/outlets/TenantListOutlet.jsx'
import ProjectListOutlet from './pages/outlets/ProjectListOutlet.jsx'

const router = createBrowserRouter([
  { id: "login", path: '/login', element: <LoginPage />, errorElement: <ErrorPage />},
  { id: "logout", path: '/logout', element: <LogoutPage />},
  { id: "help", path: '/help', element: <HelpPage />},
  { id: "license", path: '/license', element: <LicensePage />},
  { id: "register-tenant", path: '/register-tenant', element: <RegisterTenantPage />},
  { id: "register-account", path: '/register-account', element: <RegisterAccountPage />},
  { id: "reset-password", path: '/reset-password', element: <ResetPasswordPage />},

  { id: "main", path: '/', element: <MainPage />, children: [

    { id: "tenant/list", path: 'tenant/list', element: <TenantListOutlet />},

    { id: "client/list", path: 'client/list', element: <UnfinishedOutlet />},

    { id: "project/list", path: 'project/list', element: <ProjectListOutlet />},
    { id: "project/create", path: 'project/create', element: <UnfinishedOutlet />},

    { id: "account/list", path: 'account/list', element: <AccountListOutlet />},
    { id: "account/register", path: 'account/register', element: <UnfinishedOutlet />},
    { id: "account/info", path: 'account/info', element: <UnfinishedOutlet />},

    { id: "administration/reports", path: 'administration/reports', element: <UnfinishedOutlet />},
    { id: "administration/synchronization", path: 'administration/synchronization', element: <UnfinishedOutlet />},
    { id: "administration/licenses", path: 'administration/licenses', element: <UnfinishedOutlet />},

    { id: "calendar/events", path: 'calendar/events', element: <UnfinishedOutlet />}
  ]},
  {  element: <NotFoundPage />}
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
