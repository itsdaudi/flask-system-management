import { useEffect, useState } from "react";

import {
  getInventory,
  addProduct,
  updateProduct,
  deleteProduct,
  lookupProduct,
} from "../api/inventoryApi";

import AddProduct from "../components/AddProduct";
import InventoryTable from "../components/InventoryTable";
import UpdateProductForm from "../components/UpdateProduct";
import SearchProduct from "../components/SearchProduct";

function Home() {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [searchResult, setSearchResult] = useState(null);

  // ----------------------------
  // Load Inventory
  // ----------------------------
  const loadInventory = async () => {
    try {
      const response = await getInventory();
      setProducts(response.data);
    } catch (error) {
      console.error("Failed to load inventory:", error);
    }
  };

  useEffect(() => {
    loadInventory();
  }, []);

  // ----------------------------
  // Add Product
  // ----------------------------
  const handleAdd = async (product) => {
    try {
      await addProduct(product);
      loadInventory();
      alert("Product added successfully.");
    } catch (error) {
      console.error(error);
      alert("Failed to add product.");
    }
  };

 
  // ----------------------------
  // Delete Product
  // ----------------------------
  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Delete this product?"
    );

    if (!confirmDelete) return;

    try {
      await deleteProduct(id);
      loadInventory();

      alert("Product deleted.");
    } catch (error) {
      console.error(error);
      alert("Delete failed.");
    }
  };

  // ----------------------------
  // Update Product
  // ----------------------------
  const handleUpdate = async (id, product) => {
    try {
      await updateProduct(id, {
        quantity: product.quantity,
        price: product.price,
      });

      setSelectedProduct(null);
      loadInventory();

      alert("Product updated.");
    } catch (error) {
      console.error(error);
      alert("Update failed.");
    }
  };

  // ----------------------------
  // Search OpenFoodFacts
  // ----------------------------
  const handleSearch = async (barcode) => {
    try {
      const response = await lookupProduct(barcode);

      setSearchResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Product not found.");
      setSearchResult(null);
    }
  };

  return (
    <div className="container">
      <h1>Inventory Dashboard</h1>

      <AddProduct onAdd={handleAdd} />

      <SearchProduct onSearch={handleSearch} />

      {searchResult && (
        <div className="card">
          <h2>OpenFoodFacts Result</h2>

          <p>
            <strong>Name:</strong>{" "}
            {searchResult.product_name}
          </p>

          <p>
            <strong>Brand:</strong>{" "}
            {searchResult.brand}
          </p>

          <p>
            <strong>Category:</strong>{" "}
            {searchResult.category}
          </p>

          <p>
            <strong>Ingredients:</strong>{" "}
            {searchResult.ingredients}
          </p>

          {searchResult.image && (
            <img
              src={searchResult.image}
              alt={searchResult.product_name}
              width="200"
            />
          )}
        </div>
      )}

      {selectedProduct && (
        <UpdateProduct
          product={selectedProduct}
          onUpdate={handleUpdate}
        />
      )}

      <div className="card">
        <h2>Inventory</h2>

        <InventoryTable
          products={products}
          onEdit={setSelectedProduct}
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default Home;