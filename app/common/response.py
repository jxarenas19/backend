from flask import jsonify

from app.common.strings import ELEMENT_NOT_EXIST


class Response(object):
    """
    Clase encargada de conformar la respuesta del servidor despues
    de a ver realizado un post,put,delete
    """

    def __init__(self, code='', error=None, data=None, message=None):
        """

        :param code: Codigo de respuesta del servidor
        :param error: Contiene el objeto "message" con los errores
        :param filters: Contiene los filtros aplicados
        :param data: Listado paginado de la informacion
        :param message: Mensaje enviado al frontend
        """
        if data is None:
            data = {}
        self.code = code
        self.error = error
        self.data = data
        self.message = message

    def get_response(self):
        return jsonify(code=self.code, error=self.error,
                       data=self.data, message=self.message)

    def reponse_no_exist_element(self):
        return jsonify(code='404', error={'id': ELEMENT_NOT_EXIST},
                       data={}, message='Not Found')
