PasswordCracker
PasswordCracker es un script en Python diseñado para realizar un ataque de diccionario o fuerza bruta sobre un sistema de autenticación web. Toma un archivo de texto con una lista de contraseñas posibles y las prueba contra una URL de inicio de sesión para encontrar la contraseña correcta.

Este script está destinado a pruebas de penetración éticas y debe ser utilizado únicamente en entornos controlados con permiso explícito para probar la seguridad de las aplicaciones web.

Características
Toma un archivo .txt con contraseñas posibles.
Realiza intentos de inicio de sesión en una URL dada.
Rápido y sencillo de usar, con configuraciones mínimas.
Permite probar múltiples contraseñas de forma automatizada.
Requisitos
Antes de ejecutar el script, asegúrate de tener instalado Python 3.x y los siguientes módulos:

requests: Para interactuar con la página web.
Puedes instalar las dependencias con el siguiente comando:

bash
Copiar
Editar
pip install requests
Instalación
1. Clonar el repositorio
Clona este repositorio en tu máquina local:

bash
Copiar
Editar
git clone https://github.com/TU-USER/PasswordCracker.git
2. Instalar dependencias
Accede al directorio del proyecto e instala las dependencias:

bash
Copiar
Editar
cd PasswordCracker
pip install -r requirements.txt
3. Configuración
Crea un archivo de texto llamado passwords.txt que contenga las posibles contraseñas (una por línea). Un ejemplo básico de archivo passwords.txt:

pgsql
Copiar
Editar
123456
password
qwerty
letmein
Asegúrate de tener acceso a la URL de inicio de sesión en la que deseas probar las contraseñas. El script está diseñado para trabajar con formularios de inicio de sesión que aceptan una solicitud POST con un nombre de usuario y una contraseña.

Uso
1. Ejecutar el script
Una vez que hayas configurado todo, ejecuta el script de la siguiente manera:

bash
Copiar
Editar
python password_cracker.py <URL> <USUARIO> <RUTA_A_PASSWORDS.txt>
<URL>: La URL de inicio de sesión en la que se probarán las contraseñas.
<USUARIO>: El nombre de usuario que se usará en el inicio de sesión.
<RUTA_A_PASSWORDS.txt>: La ruta al archivo de contraseñas que contiene las posibles combinaciones.
Ejemplo de ejecución:
bash
Copiar
Editar
python password_cracker.py http://example.com/login admin passwords.txt
2. Resultado
El script intentará iniciar sesión con cada una de las contraseñas en el archivo passwords.txt. Si encuentra la contraseña correcta, lo notificará.

Solución de problemas
Error: Error de conexión
Asegúrate de que la URL proporcionada sea accesible y de que el formulario de inicio de sesión esté correctamente configurado para aceptar solicitudes POST.

Error: Contraseña no encontrada
Si el script no encuentra la contraseña correcta, asegúrate de que el archivo passwords.txt esté bien formateado y que la contraseña correcta esté incluida en el archivo.

Contribuciones
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del proyecto.
Crea una nueva rama para tu característica o corrección:
bash
Copiar
Editar
git checkout -b feature-XYZ
Realiza tus cambios y haz commit:
bash
Copiar
Editar
git commit -am 'Añadir nueva característica'
Haz push de tus cambios a tu rama:
bash
Copiar
Editar
git push origin feature-XYZ
Abre un pull request en GitHub para que tu contribución sea revisada.
Licencia
Este proyecto está licenciado bajo la MIT License.

Advertencia
Este script debe ser utilizado exclusivamente en pruebas de penetración éticas y autorizadas. El uso sin permiso para intentar acceder a sistemas ajenos es ilegal y puede tener consecuencias legales graves. Asegúrate de tener autorización explícita antes de utilizar este script en cualquier sistema.
