from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import pytest


@pytest.fixture
def stock():
    return [
        {
            "id": 8,
            "nome_do_produto": "dolores",
            "nome_da_empresa": "Jesus",
            "data_de_fabricacao": "2022-10-17",
            "data_de_validade": "2022-11-29",
            "numero_de_serie": 8,
            "instrucoes_de_armazenamento": "Voluptatem quo veniam nam.",
        },
        {
            "id": 9,
            "nome_do_produto": "consequatur",
            "nome_da_empresa": "Nascimento S.A.",
            "data_de_fabricacao": "2022-10-17",
            "data_de_validade": "2022-11-29",
            "numero_de_serie": 9,
            "instrucoes_de_armazenamento": "Mollitia laborum eveniet at sit.",
        },
        {
            "id": 10,
            "nome_do_produto": "veritatis",
            "nome_da_empresa": "Nascimento S.A.",
            "data_de_fabricacao": "2022-10-17",
            "data_de_validade": "2022-11-29",
            "numero_de_serie": 10,
            "instrucoes_de_armazenamento": "Sunt soluta inventore laborum.",
        },
        {
            "id": 11,
            "nome_do_produto": "soluta",
            "nome_da_empresa": "Pinto Melo - EI",
            "data_de_fabricacao": "2022-09-17",
            "data_de_validade": "2022-11-07",
            "numero_de_serie": 11,
            "instrucoes_de_armazenamento": "Minima nulla inventore doloremqu.",
        },
    ]


def test_decorar_relatorio(stock):
    GREEN = "\033[32m"
    BLUE = "\033[36m"
    RED = "\033[31m"
    END = "\033[0m"

    content_expected = (
        f"{GREEN}Data de fabricação mais antiga:{END} {BLUE}2022-09-17{END}\n"
        f"{GREEN}Data de validade mais próxima:{END} {BLUE}2022-11-07{END}\n"
        f"{GREEN}Empresa com mais produtos:{END} {RED}Nascimento S.A.{END}"
    )

    colored_simples_report = ColoredReport(SimpleReport)
    colored_complete_report = ColoredReport(CompleteReport)

    simples_report = colored_simples_report.generate(stock)
    complete_report = colored_complete_report.generate(stock)

    assert content_expected in simples_report
    assert content_expected in complete_report
