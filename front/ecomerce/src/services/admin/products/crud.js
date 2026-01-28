import { api } from '../../http/instance'


export async function createProduct(name, stock, category_id, price, is) {
    try {
        const response = await api.post(`products/product`, {
            name:name,
            stock:stock,
            category_id:category_id,
            price:price,
            is_active:true
        })
        return response.data
    } catch (error) {
        if (error.response) {
            return { erro: error.response.data.detail }
        }
        return { erro: error.message }
    }
}
