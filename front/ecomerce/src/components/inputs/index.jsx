import styles from "./input.module.css"

function Input({type, placeholder, value, onChange}){
    return (
        <>
        <input 
        type={type} 
        placeholder={placeholder} 
        value={value}
        onChange={onChange}
        className={styles.input}
        />
        </>
    )
}
export default Input