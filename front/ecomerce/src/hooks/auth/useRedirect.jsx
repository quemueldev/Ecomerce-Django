import { useNavigate } from "react-router-dom"
import { useAuth } from '../../../context/AuthContext'
import useLogin from "../../../hooks/auth/useLogin"

export default function useRedirect(email, password) {

    const navigate = useNavigate()
    const { saveUser } = useAuth()
    const { status, Login} = useLogin()


    async function redirect(){
        const user = await Login(email, password)
        console.log(user)
        if(user){
            saveUser(user)
            if(user.e_admin){
                navigate('/admin/dashboard')
            }else{
                navigate('/')
            }
        }
    }
    return { status, redirect }
}