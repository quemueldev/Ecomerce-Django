import axios from "axios"

const URL = "/api/auth"


export async function generateCode(email){
    try{
    const resp = await axios.post(`${URL}/codigo/`, {
    email:email
    })

    return resp.data
    
    } catch (error){
        if (error.response){
            return {
                erro:error.response.data.detail, 
                status: error.response.status
            }
        }
        return {erro:error.message}
    }
}

export async function verifyCode(email,code){
    console.log(`email: ${email}, code: ${code}`)
    try{
        const req = await axios.post(`${URL}/verifica_codigo/`,{
            email:email,
            code:code
        })
        return req.data
    }catch (error){
        if (error.response){
            return {
                erro: error.response.data.detail,
                status: error.response.status
            }
        }
        return {erro:error.message}
    }
}

export async function verificarToken(email,code){
    try{
        const req = await fetch(`${URL}/verifica_codigo`,{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email:email,
                code:code
            }),
        }) 
        const resp = await req.json()
        if (!req.ok){
            return {erro : resp.detail}
        }
        return resp // token
    } catch (error){
        return {erro : error}
    }
}
