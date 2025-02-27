def register_product():
    try:
        print("\n  -- Sistema Nexus --")
        name = str(input(" * Digita o nome: "))
        price = float(input(" * Digite o preço: "))
        quantity = int(input(" * Digite a quantidade: "))
        print("\n  -- Produto cadastrado com sucesso -- ")
    except ValueError as E:
        print("\n  -- Erro no cadastro. Tente novamente -- ")

    product_data = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return product_data

def delete_product():
    print("\n  -- Sistema Nexus --")
    id_product = int(input(" * Digite o id do produto que deseja deletar: "))
    return id_product

def search_product_name():
    print("\n  -- Sistema Nexus --")
    name_product = str(input(" * Digite o nome do procuto que deseja consultar: "))
    return name_product


