import os
import shutil
import smtplib

# Directorio de logs
log_dir = "ruta/a/directorio/de/logs"

# Directorio de errores
error_dir = "ruta/a/directorio/de/errores"

# Buscamos los logs en el directorio
logs = os.listdir(log_dir)

# Iteramos sobre los logs
for log in logs:
    # Verificamos si el log contiene la palabra "error"
    if "error" in log.lower():
        # Si contiene la palabra "error", copiamos el log al directorio de errores
        shutil.copy(os.path.join(log_dir, log), error_dir)
        # Enviamos un correo electrónico al administrador informándole del error
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("tu_correo@gmail.com", "tu_contraseña")
        server.sendmail("tu_correo@gmail.com", "correo_administrador@gmail.com", f"Se ha encontrado un error en el archivo {log}.")
        server.quit()
    else:
        # Si no contiene la palabra "error", eliminamos el log
        os.remove(os.path.join(log_dir, log))
         