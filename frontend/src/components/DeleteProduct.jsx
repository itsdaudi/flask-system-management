function DeleteProduct({ product, onDelete }) {

    if (!product) return null;

    return (

        <div className="card">

            <h3>

                Delete {product.product_name}?

            </h3>

            <button
                style={{ background: "red" }}
                onClick={() => onDelete(product.id)}
            >
                Delete
            </button>

        </div>

    );

}

export default DeleteProduct;