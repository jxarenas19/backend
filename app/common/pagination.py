import math

from database import DBConnection


class PaginationData(object):
    """
    Clase encargada de la pagination de los objetos de los modelos
    """

    def __init__(self, model, current_page, cant_element):
        self.model = model
        self.current_page = current_page
        self.cant_element = cant_element
        self.total = 0
        self.conn = DBConnection()
        self.session = self.conn.get_session()

    def get_pagination_data(self):
        """
        Datos generales de la paginacion
        :return:
        """
        return {
            "current_page": self.current_page,
            "next_page": self.current_page + 1,
            "prev_page": self.current_page - 1 if self.current_page - 1 != 0 else 1,
            "last_page ": math.ceil(self.total / self.cant_element),
            "cant_element ": self.cant_element,
        }

    def get_data_paginate(self):
        """
        Metodo encargado de retornar los datos paginados (en este caso es
        scroll infinito y siempre comenzara a listar desde 0 hasta el valor deseado)
        :return: Listado del modelo dado segun los datos de la paginacion
        """

        all_element = self.model_query().all()
        all_element.reverse()
        if self.current_page != '' and self.cant_element != '':
            init = self.cant_element * (self.current_page - 1)
            end = init + self.cant_element
            self.total = len(all_element)
            if end > len(all_element):
                end = len(all_element)
            all_element = all_element[init:end]
        return all_element

    def get_data_relation_paginate(self, identifier_profile):
        """
        Metodo encargado de retornar los datos paginados de una realacion (en este caso es
        scroll infinito y siempre comenzara a listar desde 0 hasta el valor deseado)
        :return: Listado del modelo dado segun los datos de la paginacion
        """
        all_element = self.model_query().filter_by(profile_id=identifier_profile).all()
        all_element.reverse()
        if self.current_page != '' and self.cant_element != '':
            init = self.cant_element * (self.current_page - 1)
            end = init + self.cant_element
            self.total = len(all_element)
            if end > len(all_element):
                end = len(all_element)
            all_element = all_element[init:end]
        return all_element

    def model_query(self):
        conn = self.conn
        session = conn.get_session()
        return session.query(self.model)

    def close_connection(self):
        try:
            self.conn.close()
            self.session.close()
        except Exception as e:
            pass
