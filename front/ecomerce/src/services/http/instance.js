import axios from 'axios'
import Cookies from 'js-cookie'

function getCookie(name) {
  return document.cookie
    .split('; ')
    .find(row => row.startsWith(name + '='))
    ?.split('=')[1]
}

export const api = axios.create({
  baseURL: "/api",
  withCredentials: true, // isso leva os cookies com a request
})

api.interceptors.request.use(config => {
  const method = config.method?.toLowerCase()
  if (!['get', 'head', 'options', 'trace'].includes(method)) {
    const csrfToken = getCookie('csrftoken')
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken
    }
  }
  return config
})

