import { api } from '../http/instance'

const URL = "http://192.168.0.15:8000/api/auth"

export async function getMyUser() {
    try {
        const resp = await api.get(`${URL}/meu_usuario/`)
        return resp.data
    } catch (error) {
        if (error.response) {
            return { erro: error.response.data.detail }
        }
        return { erro: error.message }
    }
}