import useStatus from "../useStatus";
import { login } from "../../services/auth/entrar";
import { getMyUser } from "../../services/auth/user";



export default function useLogin() {
  
    const { status, updateStatus } = useStatus()

    async function Login(email, password) {
        try {
            const response = await login(email, password)
            updateStatus(response.retorno)
            return response.user
        } catch (err) {
            updateStatus({ erro: 'Falha ao logar' })
            return null
        }
    }
    return { status, Login }    
}