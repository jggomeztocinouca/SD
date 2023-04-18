# Ejercicio 1
## Probar los ejemplos de la carpeta Examples disponible en el Campus Virtual.
### - Ejemplos de peticiones get: *openWeatherMap-example.py* y *cars-example.py*
### - Ejemplo de petición post: *pastebin-example.py*
### - Ejemplo de petición put: *renameNames-example.py*
### - Ejemplo con varios route (endpoints): *twoRoutes-example.py*
### - Ejemplo de comprobación de tipo de parámetros: *checkParameters-example.py*
### - Ejemplo de servidor y cliente con clases y varios métodos: *subjectsServer-example.py* y *subjectsClient-example.py*
#### Nota: Usar el comando curl es el comando para transferir datos hacia o desde un servidor, utilizando cualquiera de los protocolos soportados. Es la abreviatura de «Client URL».
### Sintaxis de uso: curl [options] [URL...]
#### Ejemplos de uso
#### Método GET:
curl localhost:8086/listCourses \
curl -X GET localhost:8086/listCourses

#### Método POST:
curl -X POST -H "Content-Type: application/json" -d '{"code": "1", "name": "bd"}' localhost:8086/addCourse

#### Método PUT:
curl -X PUT -H "Content-Type: application/json" -d '{"code": "1", "name": "sd"}' localhost:8086/updateCourse/1
