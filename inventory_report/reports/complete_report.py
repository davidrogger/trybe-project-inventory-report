from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventories):
        simple_report = super().generate(inventories)
        companies_count = cls.count_companies(inventories)
        additional_report = "Produtos estocados por empresa:\n"

        for company in inventories:
            company_name = company["nome_da_empresa"]
            if company_name not in additional_report:
                additional_report += (
                    f"- {company_name}: {companies_count[company_name]}\n"
                )

        return f"{simple_report}\n" f"{additional_report}"
