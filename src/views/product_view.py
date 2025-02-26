class ProductView:
    def register_product(self):
        try:
            name = str(input("Digita o nome: "))
            price = float(input("Digite o preço: "))
            quantity = int(input("Digite a quantidade: "))
        except ValueError as E:
            print(f"Tipo de dado inválido no registro. Tente novamente.")

        product_data = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        return product_data





