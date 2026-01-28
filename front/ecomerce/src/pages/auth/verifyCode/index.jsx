import { useState } from 'react'
import { useVerifyCode } from '../../../hooks/useToken'
import { useNavigate, useLocation } from 'react-router-dom'
import { useRegister } from '../../../hooks/auth/useRegister'



function VerifyCode() {
  const handleVerify = async () => {
    const req = await VerifyCode(email, code)
    if(req){
      const user = await register(email, name, password)
      if (user) {navigate('/home')}
      else {alert('erro ao cadastrar')}
    }
  }


  const { status, VerifyCode } = useVerifyCode()
  const {register} = useRegister()

  const navigate = useNavigate()
  const location = useLocation()
  const {email, name, password} = location.state || {}
  console.log(`${email},${name}, ${password}`)
  const [code, setCode] = useState('')

  return (
    <div>
      <h1>verify</h1>
      <p>email: {email}</p>
      <input type='text' value={code} onChange={(e) => setCode(e.target.value)} />
      <button onClick={handleVerify}>
        verificar
      </button>
      <button onClick={() => navigate(-1)}>
        voltar
      </button>
    </div>
  )
}

export default VerifyCode
