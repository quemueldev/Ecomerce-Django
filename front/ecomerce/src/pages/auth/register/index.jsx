import { useNavigate } from "react-router-dom"
import { useState } from "react"
import Input from "../../../components/inputs"
import { useGenerateToken } from '../../../hooks/useToken'


function Register(){
    
    const navigate = useNavigate()
    const {status, GenerateToken} = useGenerateToken()
    
    const [email, setEmail] = useState('')
    const [name, setName ] = useState('')
    const [password, setPassword] = useState('')
    const [showPassword, setShowPassword] = useState(false)
    return(
        <div>

        <p>ola cadastro</p>
        <Input 
        type='email'
        placeholder='email'
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        />
        <Input 
        type='text'
        placeholder='nome'
        value={name}
        onChange={(e) => setName(e.target.value)}
        />
        <Input 
        type={showPassword ? 'text': 'password'}
        placeholder='senha'
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={() => setShowPassword(!showPassword)}>
            olhinho
        </button>
        <button onClick={async () => {
        const req = await GenerateToken(email)
        if (req){
          navigate('/verify_code', {state: {email: email,name :name, password:password}})
        }
        }}>
          Enviar
      </button>
        

        <button onClick={() => navigate(-1)} >
            voltar
        </button>
        </div>
    )
}
export default Register