Este script se utiliza para probar webhooks salientes y comandos slash de Mattermost.

Para ejecutar, es necesario tener Python 3+ y Flask. Se recomienda crear un virtualenv
en la carpeta e instalar la biblioteca necesaria con `pip install -r requirements.txt`.

Las URLs de prueba son:
* `/`: Si es una solicitud tipo POST, se muestra por consola el payload enviado.
* `/ping`: Responde con contenido JSON que genera un mensaje en Mattermost con el contenido "pong".

Nota: Este script no verifica los token de Mattermost.
