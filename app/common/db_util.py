
from sqlalchemy import text

from database import DBConnection

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatabaseUtils:
    def __init__(self, element='', model=''):
        self.conn = DBConnection()
        self.element = element
        self.model = model
        self.session = self.conn.get_session()

    def save(self):
        self.session.add(self.element)
        self.session.commit()


    def delete(self):
        self.session.delete(self.element)
        self.session.commit()

    def update(self, update_values):
        for key, value in update_values.items():
            if value is not None:
                setattr(self.element, key, value)
        try:
            self.session.add(self.element)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise

    def update_many_variants(self, variants):
        """
        Agregar una lógica para actualizar las variantes asociadas a un producto
        :param variants:
        :return:
        """
        pass

    def get_all(self):
        return self.model_query().all()

    def get_by_id(self, id):
        self.element = self.model_query().get(id)
        return self.element

    def simple_filter(self, **kwargs):
        return self.model_query().filter_by(**kwargs).all()

    def filter_by(self, **kwargs):
        return self.model_query().filter_by(**kwargs)

    def raw_query(self, product_id):
        raw_query = text("SELECT * FROM vista_listado_products_global_1_product_id  WHERE product_id = :val ")
        result = self.session.execute(raw_query, {"val": product_id})
        return result

    def format_text(self, value):
        return '\'' + value + '\''

    def raw_query1(self, product_id, variants, dimensions):
        raw_query = text(
            "SELECT * FROM vista_listado_products_global_2_product_id WHERE product_id = :val "
            + " AND value  IN (%s)" % ",".join(map(self.format_text, variants))
            + " AND name IN (%s)" % ",".join(map(self.format_text, dimensions))
        )

        result = self.session.execute(raw_query, {"val": product_id})
        return result

    def raw_query2(self, product_id):
        raw_query = text(
            "SELECT * FROM vista_listado_products_global_3_product_id WHERE product_id = :val "
        )

        result = self.session.execute(raw_query, {"val": product_id})
        return result

    def raw_query3(self, product_id):
        raw_query = text(
            "SELECT * from products_global WHERE product_id = :val "
        )

        result = self.session.execute(raw_query, {"val": product_id})
        return result

    def get_by_id_specific(self, **kwargs):
        self.element = self.model_query().filter_by(**kwargs).first()
        return self.element

    def model_query(self):
        conn = self.conn
        session = conn.get_session()
        return session.query(self.model)

    def model_query_performe(self, model):
        conn = self.conn
        session = conn.get_session()
        return session.query(model)

    def close_connection(self):
        try:
            self.conn.close()
            self.session.close()
        except Exception as e:
            pass
