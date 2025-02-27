from src.views.product_view import register_product, delete_product, search_product_name
from src.controllers.product_controller import ProductController

def options_decision():
    message = """
    \n
          NEXUS SOFTWARE 
    ( ======================= )
    *   -- Sistema Nexus --   *
    *                         *
    *  [0] Sair               *
    *  [1] Cadastrar Produto  *
    *  [2] Excluir Produto    *
    *  [3] Todos os Produtos  *
    *  [4] Buscar Produto     *
    *                         *
    ( ======================= )
    """
    return message

def menu_decision():
    while True:
        print(options_decision())
        command = int(input(" * Escolha: "))
        if command == 0: exit()
        if command == 1:
            controller = ProductController()
            data = register_product()
            data_name = data.get("name")
            data_price = data.get("price")
            data_quantity = data.get("quantity")
            controller.add_product(data_name, data_price, data_quantity)
        if command == 2:
            id_product = delete_product()
            controller = ProductController()
            controller.delete_product(id_product)
        if command == 3:
            controller = ProductController()
            print(controller.all_products())
        if command == 4:
            controller = ProductController()
            product_name = search_product_name()
            controller.search_product(product_name)

