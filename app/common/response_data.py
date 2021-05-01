from flask import jsonify


class ResponseData(object):
    """
    Clase encargada de conformar la respuesta del servidor
    """

    def __init__(self, code, error, filters, data, pagination):
        """

        :param code: Codigo de respuesta del servidor
        :param error: Contiene el objeto "message" con los errores
        :param filters: Contiene los filtros aplicados
        :param data: Listado paginado de la informacion
        :param pagination: Datos generales de la paginacion
        """
        self.code = code
        self.error = error
        self.filters = filters
        self.data = data
        self.pagination = pagination

    def get_response(self):
        return jsonify(code=self.code, error=self.error,
                       filters=self.filters, data=self.data,
                       pagination=self.pagination)
