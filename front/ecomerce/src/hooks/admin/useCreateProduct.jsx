import { createProduct } from '../../services/admin/products/crud'
import useStatus from '../useStatus'

export function useCreateProduct() {
   const { status, updateStatus } = useStatus()

   async function CreateProduct(name, stock, category_id, price, is_active) {
        try {
            
            const req = await createProduct(name, stock, category_id, price, is_active)

            updateStatus(req)
        } catch (error) {
            if (error.response){
                updateStatus({ erro: error.response.data.detail })
            } 
            updateStatus({ erro: error.message })
        }
   }
   return { status, CreateProduct }
}