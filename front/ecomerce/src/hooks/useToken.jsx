import useStatus from "./useStatus"
import { generateCode, verifyCode } from '../services/auth/token'

export function useGenerateToken() {
   const { status, updateStatus } = useStatus()

   async function GenerateToken(email) {
    try {
    const resp = await generateCode(email)
    updateStatus(resp)

    return !resp.erro
    } catch {
    updateStatus({ erro: 'Falha ao gerar token' })
    return false
    }
   }

   return { status, GenerateToken }
}

export function useVerifyCode(){
    const { status, updateStatus } = useStatus()

    async function VerifyCode(email, code) {

    try {
    const resp = await verifyCode(email, code)
    updateStatus(resp)

    return !resp.erro
    } catch {
    updateStatus({ erro: 'Falha ao verificar codigo' })
    return false
    }

   }

   return { status,  VerifyCode}
}