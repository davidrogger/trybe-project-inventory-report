from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventories: list):
        older_manufacture_date = cls.get_older_manufacture_date(inventories)

        near_expire_date = cls.get_near_expite_date(inventories)
        company_with_more_products = cls.get_company_with_most_products(
            inventories
        )

        return (
            f"Data de fabricação mais antiga: {older_manufacture_date}\n"
            f"Data de validade mais próxima: {near_expire_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @classmethod
    def get_older_manufacture_date(cls, inventories):
        manufacture_dates = cls.create_list_of_dates(
            inventories, "data_de_fabricacao"
        )
        older_date = min(manufacture_dates)
        return older_date.isoformat()

    @classmethod
    def get_near_expite_date(cls, inventories):
        today = date.today()
        expire_dates = cls.create_list_of_dates(
            inventories, "data_de_validade"
        )
        valid_expire_dates = [date for date in expire_dates if date >= today]
        near_date = min(valid_expire_dates)
        return near_date.isoformat()

    @classmethod
    def create_list_of_dates(cls, inventories, field):
        return [
            date.fromisoformat(inventory[field]) for inventory in inventories
        ]

    @classmethod
    def get_company_with_most_products(cls, inventories):
        company_names = [
            inventory["nome_da_empresa"] for inventory in inventories
        ]
        count_companies = Counter(company_names).most_common()
        first_from_the_count = count_companies[0][0]
        return first_from_the_count
