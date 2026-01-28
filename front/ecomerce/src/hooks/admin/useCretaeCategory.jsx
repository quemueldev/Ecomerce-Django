import { createCategory } from '../../services/admin/products/categories/crud'
import useStatus from '../useStatus'


export function useCreateCategory(name) {

   
   const { status, updateStatus } = useStatus()

   async function CreateCategory(name) {
    
        try {
            const req = await createCategory(name)
            updateStatus(req)
        } catch (error) {
            if (error.response){
                updateStatus({ erro: error.response.data.detail })
            } 
            updateStatus({ erro: error.message })
        }
   }
   return { status, CreateCategory }
}