import { useState } from "react";

function AddProductForm({ onAdd }) {

    const [product, setProduct] = useState({

        barcode: "",

        product_name: "",

        brand: "",

        category: "",

        quantity: "",

        price: ""

    });

    const handleChange = (e) => {

        setProduct({

            ...product,

            [e.target.name]: e.target.value

        });

    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onAdd(product);

        setProduct({

            barcode: "",

            product_name: "",

            brand: "",

            category: "",

            quantity: "",

            price: ""

        });

    };

    return (

        <form onSubmit={handleSubmit} className="card">

            <h2>Add Product</h2>

            <input
                name="barcode"
                placeholder="Barcode"
                value={product.barcode}
                onChange={handleChange}
            />

            <input
                name="product_name"
                placeholder="Product Name"
                value={product.product_name}
                onChange={handleChange}
            />

            <input
                name="brand"
                placeholder="Brand"
                value={product.brand}
                onChange={handleChange}
            />

            <input
                name="category"
                placeholder="Category"
                value={product.category}
                onChange={handleChange}
            />

            <input
                name="quantity"
                placeholder="Quantity"
                type="number"
                value={product.quantity}
                onChange={handleChange}
            />

            <input
                name="price"
                placeholder="Price"
                type="number"
                value={product.price}
                onChange={handleChange}
            />

            <button>Add Product</button>

        </form>

    );

}

export default AddProductForm;