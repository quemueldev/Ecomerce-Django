import { createContext, useContext, useState } from 'react'

const authContext = createContext(null)

export function authProvider({ children }) {
  const [usuario, setUsuario] = useState(null)

  // Função que salva o usuário no estado global
  const saveUser = (dadosUsuario) => {
    setUsuario(dadosUsuario)
  }

  return (
    <authContext.Provider value={{ usuario, saveUser }}>
      {children}
    </authContext.Provider>
  )
}

export function useAuth() {
  return useContext(authContext)
}
