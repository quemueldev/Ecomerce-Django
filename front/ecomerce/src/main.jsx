import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import "./services/http/index"


import VerifyCode from './pages/auth/verifyCode'
import Index from './pages/home/index'
import Register from './pages/auth/register'
import Login from './pages/auth/login'
import { createBrowserRouter,RouterProvider } from 'react-router-dom'
import HomeAdmin from './pages/admin/dashborad'

import RouteAdmin from './routes/adminRoute'
import { authProvider as AuthProvider } from './context/AuthContext'
import ProductsAdmin from './pages/admin/products'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Index />,
  },
  {
    path: '/verify_code',
    element: <VerifyCode />,
  },
  {
    path: '/register',
    element: <Register />
  },
  {
    path: '/login',
    element: <Login />
  },
  
  {
    path: '/admin/dashboard',
    element: (
      <RouteAdmin>
        <HomeAdmin />
      </RouteAdmin>
    )
  },
  {
    path: '/admin/products',
    element: (
      <RouteAdmin>
        <ProductsAdmin />
      </RouteAdmin>
    ),
  }

])

createRoot(document.getElementById('root')).render(
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
)
