from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)

        companies_counter = cls.get_companies(list)

        description = "\nProdutos estocados por empresa:\n"

        for company, quantity in companies_counter.items():
            description += f"- {company}: {quantity}\n"

        return simple_report + description
