import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:5000"
});

// Inventory CRUD

export const getInventory = () =>
    API.get("/inventory");

export const getProduct = (id) =>
    API.get(`/inventory/${id}`);

export const addProduct = (product) =>
    API.post("/inventory", product);

export const updateProduct = (id, product) =>
    API.patch(`/inventory/${id}`, product);

export const deleteProduct = (id) =>
    API.delete(`/inventory/${id}`);

export const lookupProduct = (barcode) =>
    API.get(`/lookup/${barcode}`);

export default API;