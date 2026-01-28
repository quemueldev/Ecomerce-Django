import useStatus from "../useStatus"
import { register } from '../../services/auth/entrar'

export function useRegister() {
   const { status, updateStatus } = useStatus()

   async function Register(email, name, password) {
      try {
         const resp = await register(email, name, password)
         updateStatus(resp.retorno)

         return !resp.erro
      } catch {
         updateStatus({ erro: 'Falha ao se cadastrar' })
         return false
      }
   }
   return { status, Register }
}