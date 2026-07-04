import { useState } from "react";

function SearchProduct({ onSearch }) {

    const [barcode, setBarcode] = useState("");

    return (

        <div className="card">

            <h2>Search OpenFoodFacts</h2>

            <input

                placeholder="Barcode"

                value={barcode}

                onChange={(e) =>
                    setBarcode(e.target.value)
                }

            />

            <button
                onClick={() => onSearch(barcode)}
            >
                Search
            </button>

        </div>

    );

}

export default SearchProduct;