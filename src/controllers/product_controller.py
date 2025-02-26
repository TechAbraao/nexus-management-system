from src.models.product_model import ProductModel, get_session

class ProductController:
    def __init__(self):
        self.session = get_session()

    def add_product(self, name, price, quantity):
        try:
            product = ProductModel(name=name, price=price, quantity=quantity)
            self.session.add(product)
            self.session.commit()
        except Exception as E:
            print(f"Erro ao cadastrar produto: {E}")

    def delete_product(self, id_product):
        product = self.session.query(ProductModel).get(id_product)
        if product:
            self.session.delete(product)
            self.session.commit()
            print("\n  -- Produto deletado com sucesso -- ")
        else:
            print(f"\n  -- Produto com id {id_product} não encontrado -- ")