function InventoryTable({
    products,
    onDelete,
    onEdit
}) {

    return (

        <table>

            <thead>

                <tr>

                    <th>ID</th>

                    <th>Name</th>

                    <th>Barcode</th>

                    <th>Quantity</th>

                    <th>Price</th>

                    <th>Actions</th>

                </tr>

            </thead>

            <tbody>

                {products.map(product => (

                    <tr key={product.id}>

                        <td>{product.id}</td>

                        <td>{product.product_name}</td>

                        <td>{product.barcode}</td>

                        <td>{product.quantity}</td>

                        <td>{product.price}</td>

                        <td>

                            <button
                                onClick={() => onEdit(product)}
                            >
                                Edit
                            </button>

                            <button
                                style={{
                                    marginLeft: 10,
                                    background: "red"
                                }}
                                onClick={() => onDelete(product.id)}
                            >
                                Delete
                            </button>

                        </td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}

export default InventoryTable;