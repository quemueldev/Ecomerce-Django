import { useNavigate } from 'react-router-dom'


function HomeAdmin(){
    const navigate = useNavigate()
    return(
        <>
        <p>ola admin</p>
        <button onClick={() => navigate('/admin/products')}>
            products
        </button>
        </>
    )
}
export default HomeAdmin