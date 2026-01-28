function FormProduct({}){
    return (
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
        </>
    )
}