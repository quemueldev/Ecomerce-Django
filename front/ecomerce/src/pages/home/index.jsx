import { useNavigate } from "react-router-dom"

export default function Index(){
    const obj =[
        {nome: 'kaka', id: 1},
        {nome: 'lele', id: 2},
        {nome: 'meme', id: 3},
        {nome: 'nene', id: 4},
        {nome: 'papa', id: 5},
        {
            nome: 'rara',
            id: 6
        },
        {nome: 'sasa', id: 7},
        {nome: 'tata', id: 8},
        {nome: 'vava', id: 9},

    ]
    const navigate = useNavigate()
    return(
        <>
        <p>kaka</p>
        {obj.map((item) => {
            return(
                <p key={item.nome}>{item.nome}</p>
            )
        })}
        <p>entrar:</p>
        <button onClick={() => navigate("/login")}>
            Ir para auth
        </button>
        
        </>
    )
}