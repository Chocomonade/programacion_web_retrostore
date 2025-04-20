import os
import cx_Oracle

# Mostrar el path usado
print("🔍 PATH:", os.environ['PATH'])

# Confirmar existencia del archivo clave
print("📂 Buscando oci.dll...")
if os.path.exists(r"C:\oracle\instantclient_23_7\oci.dll"):
    print("✅ oci.dll encontrado")
else:
    print("❌ oci.dll no encontrado")

try:
    print("🚀 Intentando conectar a Oracle...")
    connection = cx_Oracle.connect(
        user="system",
        password="Oracle1234",
        dsn="localhost/XE"
    )
    print("✅ Conexión exitosa 🎉")
    print("Versión del servidor:", connection.version)
    connection.close()

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("❌ ERROR:", error.message)

except Exception as e:
    print("⚠️ Excepción inesperada:", str(e))
