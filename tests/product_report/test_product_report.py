from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    company_name = "Casa e camas"
    product_name = "Cama"
    manufacturing_date = "2022-10-28"
    expiration_date = "2023-10-28"
    serial_number = "123456789"
    store_instructions = "Coberto contra sol e chuva"

    valid_representation = (
        f"O produto {product_name}"
        f" fabricado em {manufacturing_date}"
        f" por {company_name} com validade"
        f" até {expiration_date}"
        f" precisa ser armazenado {store_instructions}."
    )

    new_product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        store_instructions,
    )

    assert str(new_product) == valid_representation
