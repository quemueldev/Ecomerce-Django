import axios from "axios"

const URL = "http://192.168.0.15:8000/api/products"

axios({
    method: 'get',
    url: `${URL}/product/`
})

axios.get("https://api.exemplo.com/users")
  .then((resp) => {
    console.log(resp)
    console.log(resp.data);
  })
  .catch(error => {
    console.error(error);
  });


axios.post("https://api.exemplo.com/users", {
  name: "João",
  email: "joao@email.com"
})
.then(res => {
  console.log(res.data);
})
.catch(err => {
  console.error(err);
});

async function buscarUsers() {
  try {
    const response = await axios.get("https://api.exemplo.com/users");
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
