

## Despliegue
Este microservicio depende de [kmodels](https://gitlab.com/manogroup/kiero/marketplace-services/kmodels) por este motivo al compilar. Es necesario pasar un [token de autorización](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) para bajar el repositorio kmodels.

En el directorio del proyecto ejecutar el siguiente comando para construir la imagen de docker:

`docker-compose build --build-arg GITLAB_TOKEN=xxxxxxxxxx`

Establecer en el archivo `.env` los valores de las variables de entorno correspondientes

En el directorio del proyecto ejecutar el siguiente comando para ejecutar el contenedor de docker:

`docker-compose up -d`

El comando anterior ejecuta un contendor del microservicio exponiendo los endpoints por el puerto 4002
