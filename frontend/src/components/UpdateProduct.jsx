import { useState, useEffect } from "react";

function UpdateProductForm({ product, onUpdate }) {

    const [form, setForm] = useState(product);

    useEffect(() => {

        setForm(product);

    }, [product]);

    if (!product) return null;

    const handleChange = (e) => {

        setForm({

            ...form,

            [e.target.name]: e.target.value

        });

    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onUpdate(form.id, form);

    };

    return (

        <form onSubmit={handleSubmit} className="card">

            <h2>Update Product</h2>

            <input
                name="quantity"
                value={form.quantity}
                onChange={handleChange}
            />

            <input
                name="price"
                value={form.price}
                onChange={handleChange}
            />

            <button>Update</button>

        </form>

    );

}

export default UpdateProductForm;