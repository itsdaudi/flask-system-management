import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:5555"
});

// Inventory CRUD

export const getInventory = () =>
    API.get("/Inventory");

export const getProduct = (id) =>
    API.get(`/Inventory/${id}`);

export const addProduct = (product) =>
    API.post("/Inventory", product);

export const updateProduct = (id, product) =>
    API.patch(`/Inventory/${id}`, product);

export const deleteProduct = (id) =>
    API.delete(`/Inventory/${id}`);

export const lookupProduct = (barcode) =>
    API.get(`/lookup/${barcode}`);

export default API;