from datetime import datetime
from ast import Dict
from collections import Counter


class SimpleReport:
    def generate(list: Dict):
        # nome da empresa
        companies = [product["nome_da_empresa"] for product in list]
        companie_bigger_stock = Counter(companies).most_common()[0][0]

        # data de fabricação
        manufacturing_dates = [
            product["data_de_fabricacao"] for product in list
        ]
        min_manufacturing_date = min(manufacturing_dates)

        # data de validade
        date_now = str(datetime.now())
        expiration_dates = [
            product["data_de_validade"] for product in list
            if product["data_de_validade"] >= date_now
        ]
        next_expiration_date = min(expiration_dates)

        return (
            f"Data de fabricação mais antiga: {min_manufacturing_date}\n"
            f"Data de validade mais próxima: {next_expiration_date}\n"
            f"Empresa com mais produtos: {companie_bigger_stock}"
        )
