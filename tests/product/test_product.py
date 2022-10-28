from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    company_name = "Casa e camas"
    product_name = "Cama"
    manufacturing_date = "2022-10-28"
    expiration_date = "2023-10-28"
    serial_number = "123456789"
    store_instructions = "Coberto contra sol e chuva"

    new_product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        store_instructions,
    )

    assert new_product.id == id
    assert new_product.nome_da_empresa == company_name
    assert new_product.nome_do_produto == product_name
    assert new_product.data_de_fabricacao == manufacturing_date
    assert new_product.data_de_validade == expiration_date
    assert new_product.numero_de_serie == serial_number
    assert new_product.instrucoes_de_armazenamento == store_instructions
