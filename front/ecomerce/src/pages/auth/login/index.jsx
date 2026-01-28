import { useNavigate } from "react-router-dom"
import { useState } from "react"
import Input from "../../../components/inputs/index"
import useLogin from "../../../hooks/auth/useLogin"
import { useAuth } from '../../../context/AuthContext'

function Login(){

    const navigate = useNavigate()

    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [showPassword, setShowPassword] = useState(false)

    

    const {status, Login} = useLogin()
    const { saveUser } = useAuth()

    const logar = async () =>{
        const user = await Login(email, password)
        console.log(user)
        console.log('cookie: ', document.cookie)
        if(user){
            saveUser(user)
            if(user.e_admin){
                navigate('/admin/dashboard')
            }else{
                navigate('/')
            }
        }
    }   


    return(
        <>
        <p>{String(status?.mensagem)}</p>
        <p>esta no lofin</p>
        <Input 
        type='email'
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="email"

        />
        <Input 
        type={showPassword ? 'text' : 'password'}
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="password"
        />
        <button onClick={() => setShowPassword(!showPassword)}>
            {showPassword ? 'esconder senha' : 'mostrar senha'}
        </button>
        <button onClick={logar}>
            entrar
        </button>


        <button onClick={() => navigate('/register')}>
            se cadastrar
        </button>
        <button onClick={() => navigate(-1)} >
            voltar
        </button>
        </>
    )
}
export default Login