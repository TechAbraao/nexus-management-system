from src.models.product_model import ProductModel, Base, get_session
def create_tables():
    Base.metadata.create_all(get_session().bind)
create_tables()
