import { api } from '../../../http/instance'
const URL = "/api/products"

export async function createCategory(name) {
    
    try {

        const response = await api.post(`products/category/`, {
            name:name,
        })
        console.log(response)
        
        return response.data
    } catch (error) {
        if (error.response) {
            return { erro: error.response.data.detail }
        }
        return { erro: error.message }
    }
}