import { Navigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function RouteAdmin({ children }) {
  const { usuario } = useAuth()

  // 1️⃣ Não logado
  if (!usuario) {
    return <Navigate to="/login" />
  }

  // 2️⃣ Logado mas não é admin
  if (!usuario.e_admin) {
    return <Navigate to="/" />
  }

  // 3️⃣ Pode entrar
  return children
}
