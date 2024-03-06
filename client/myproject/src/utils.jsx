import axios from "axios"

const getAll = async (url) => {
    const response = await axios.get(url)
    return response.data
}



const addItem = async (url, item) => {
    const response = await axios.post(url, item)
    // console.log(response.data)
    return response.data
}

const updateItem = async (url, item) => {
    const response = await axios.put(url, item)
    console.log(response.data)
    return response.data
}

const deleteItem = async (url) => {
    const response = await axios.delete(url)
    // console.log(response.data)
    return response.data
}



export { getAll, addItem, deleteItem, updateItem }