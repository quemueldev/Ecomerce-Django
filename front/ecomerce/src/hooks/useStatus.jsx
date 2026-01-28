import { useState } from "react"

export default function useStatus() {
   const [status, setStatus] = useState([])

   function updateStatus(msg) {
     if (msg.erro) {
       setStatus(msg.erro)
     } else {
       setStatus(msg.retorno)
     }

     setTimeout(() => setStatus([]), 2000)
   }

   return { status, updateStatus }
}
