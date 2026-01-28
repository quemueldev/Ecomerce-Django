// services/http/auth.interceptor.js
import { api } from './instance'

let estaAtualizando = false
let filaPendente = []

/**
 * Processa a fila de requisições que estavam esperando o refresh
 * @param {any} erro - erro caso o refresh tenha falhado
 */
function processarFila(erro = null) {
  filaPendente.forEach(({ rejeitar }) => rejeitar(erro))
  filaPendente = []
}

/**
 * Configura o interceptor de autenticação
 * @param {function} logout - função que realiza logout (redireciona para login)
 */
export function interceptor(logout) {
  api.interceptors.response.use(
    resposta => resposta,
    async erro => {
      const requisicaoOriginal = erro.config

      // se não for 401, apenas rejeita
      if (erro.response?.status !== 401) {
        return Promise.reject(erro)
      }

      // se já tentou refresh, faz logout
      if (requisicaoOriginal._retry) {
        logout()
        return Promise.reject(erro)
      }

      requisicaoOriginal._retry = true

      // se já está atualizando o token, adiciona a fila e espera
      if (estaAtualizando) {
        return new Promise((_, rejeitar) => {
          filaPendente.push({ rejeitar })
        })
      }

      estaAtualizando = true

      try {
        // tenta atualizar o token
        await api.post('/core/refresh/')

        estaAtualizando = false

        // processa fila de requisições pendentes
        processarFila()

        // refaz a requisição original
        return api(requisicaoOriginal)
      } catch (err) {
        // se falhar o refresh → rejeita fila e faz logout
        estaAtualizando = false
        processarFila(err)
        logout()
        return Promise.reject(err)
      }
    }
  )
}
