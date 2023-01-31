from inventory_report.inventory.product import Product


def test_cria_produto():
   product = Product(1, "celular", "vivo", "31-01-2023", "31-01-2028", "123464783100014", "Não utilizar quando estiver carregando")
   
   assert product.id == 1
   assert product.nome_do_produto == "celular"
   assert product.nome_da_empresa == "vivo"
   assert product.data_de_fabricacao == "31-01-2023"
   assert product.data_de_validade == "31-01-2028"
   assert product.numero_de_serie == "123464783100014"
   assert product.instrucoes_de_armazenamento == "Não utilizar quando estiver carregando"


