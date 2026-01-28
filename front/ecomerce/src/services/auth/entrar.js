import axios from "axios"

const URL = "/api/auth"

export async function register(email, name, password){
    try{
        const req = await axios.post(`${URL}/cadastro/`,{
            email:email,
            name:name,
            password:password,
        })
        return req.data
    } catch (error){
        if (error.response){
            return {erro: error.response.data.detail}
        }
        return {erro:error.message} 
    }
}

export async function login(email, password){
    try{
        const req = await axios.post(`${URL}/login/`,{
            email:email,
            password:password,
        })
        return req.data
    } catch (error){
        if (error.response){
            return {erro: error.response.data.detail}
        }
        return {erro:error.message} 
    }
}