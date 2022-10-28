from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventories):
        companies_count = cls.count_companies(inventories)
        company_counter = "Produtos estocados por empresa:\n"

        for company in inventories:
            company_name = company["nome_da_empresa"]
            if company_name not in company_counter:
                company_counter += (
                    f"- {company_name}: {companies_count[company_name]}\n"
                )

        return f"{super().generate(inventories)}\n" f"{company_counter}"
