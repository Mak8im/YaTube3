axios.get("http://localhost:8000/api/lenta")
.then((response) => {
    console.log(response.data)
})
.catch((e) => {
    console.warn(e)
})