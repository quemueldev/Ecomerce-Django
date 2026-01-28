import { useNavigate } from 'react-router-dom'
import { useCreateProduct } from '../../hooks/admin/useCreateProduct'
import { useState }from 'react'
import Input from '../../components/inputs'
import { useCreateCategory } from '../../hooks/admin/useCretaeCategory'

export default function ProductsAdmin(){
    const navigate = useNavigate()
    const { status, CreateProduct } = useCreateProduct()
    const { CreateCategory } = useCreateCategory()

    const [menuProducts, setMenuProducts] = useState(false)

    const [nome, setNome] = useState('')
    const [nomeCategory, setNomeCategory] = useState('')
    const [stock, setStock] = useState(0)
    const [category_id, setCategoryId] = useState(0)
    const [preco, setPreco] = useState(0)
    const [is_active, setIsActive] = useState(true)

    const handleCreateProduct = async () => {
        await CreateProduct(nome, stock, category_id, preco, is_active)
    }
    const handleCreateCategory = async () => {
        
        await CreateCategory(nomeCategory)
    }

    return(
        <>
        {menuProducts && (
            <>
            <Input 
            type='text'
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            placeholder="nome do produto"
        />
        <Input 
            type='number'
            value={stock}
            onChange={(e) => setStock(Number(e.target.value))}
            placeholder="stock"
        />
        <Input 
            type='number'
            value={category_id}
            onChange={(e) => setCategoryId(Number(e.target.value))}
            placeholder="category id"
        />
        <Input 
            type='number'
            value={preco}
            onChange={(e) => setPreco(Number(e.target.value))}
            placeholder="preco"
        />
        <button onClick={() => setIsActive(!is_active)}>
            {is_active ? 'ativo' : 'inativo'}
        </button>
        <button onClick={handleCreateProduct}>
           criar produto
        </button>

        </>
        )}
        <button onClick={() => setMenuProducts(!menuProducts)}>
            {menuProducts ? 'fechar menu' : 'abrir menu de produtos'}
        </button>

        <input 
            type='text'
            value={nomeCategory}
            onChange={(e) => setNomeCategory(e.target.value)}
            placeholder="nome da categoria"
        />
        <button onClick={handleCreateCategory}>
           criar categoria
        </button>

        

        


        <p>{String(status?.mensagem)}</p>
        <h1>Products Admin</h1>
        <button onClick={() => navigate(-1)}>

        </button>
        </>
    )
}