import { interceptor } from './interceptor'
import { logout } from './logout'

interceptor(logout)

export { api } from './instance'
