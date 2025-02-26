from src.views.product_view import ProductView
from src.controllers.product_controller import ProductController

def options_decision():
    message = """
    1 - Cadastrar produto
    2 - Excluir produto
    """
    return message

def menu_decision():
    while True:
        print(options_decision())
        command = int(input("Qual opção deseja efetuar: "))
        if command == 1:
            product = ProductView()
            controller = ProductController()

            data = product.register_product()
            data_name = data.get("name")
            data_price = data.get("price")
            data_quantity = data.get("quantity")
            controller.add_product(data_name, data_price, data_quantity)

