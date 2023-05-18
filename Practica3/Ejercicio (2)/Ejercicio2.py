from bottle import route, run, request, HTTPResponse
# route → Define las rutas de la aplicación web
# run → Inicia el servidor
# request → Información sobre la solicitud HTTP entrante
# HTTPResponse → Crea respuestas HTTP personalizadas.

import json # Para trabajar con datos JSON

mis_elementos = [] # Esta lista se utilizará para almacenar los elementos enviados a través de las solicitudes POST.

@route('/inserta', method='POST') # Definición de la ruta /inserta que responderá a las solicitudes POST.
def inserta(): # Definición de la función contenida en la ruta inserta
    try: # Para manejar las excepciones que pueden surgir durante la ejecución del código dentro de este bloque.
        data = request.json
        # Aquí, estamos tomando el cuerpo de la solicitud HTTP entrante, de formato JSON, y lo estamos convirtiendo en un objeto Python.
        # request.json automáticamente convierte el cuerpo JSON de la solicitud en un diccionario Python.
        if 'elemento' not in data: # Comprobamos si la clave 'elemento' no está presente en los datos de la solicitud.
            return HTTPResponse(status=400, body='No se proporcionó la clave "elemento"') # De ser así, se produce una excepción.
            # Códigos de respuesta HTTP:
            # Respuestas informativas (100–199),
            # Respuestas satisfactorias (200–299),
            # Redirecciones (300–399),
            # Errores de los clientes (400–499),
            # y errores de los servidores (500–599).
        else: # Si está...
            elemento = data['elemento'] # ... almacenamos el número con clave 'elemento' en la variable elemento.
            if elemento not in mis_elementos: # Si elemento no se encuentra ya añadido en la lista (tolerancia a redundancia)...
                mis_elementos.append(elemento) # ... lo añadimos a la lista
            return {"mis_elementos": mis_elementos} # Devuelve al cliente el diccionario con el elemento añadido.
    except Exception as e: # Si se produce algún error...
        return HTTPResponse(status=500, body='Error inesperado') # ... devuelve el error correspondiente.

run(host='localhost', port=8080) # Inicia el servidor en un host (localhost) con puerto a la escucha (8000)
