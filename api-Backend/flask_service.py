# Al ejecutar flask_service.py, se creará una instancia de la aplicación Flask y se iniciará el servidor web 
# para que la aplicación esté disponible en la dirección IP pública del servidor en el puerto 80. Además, se 
# habilita el modo de depuración con el parámetro debug=True, lo que permite ver información detallada sobre 
# los errores en la aplicación en caso de que ocurran.
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
