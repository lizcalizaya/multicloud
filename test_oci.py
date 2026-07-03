import os
from pathlib import Path
from dotenv import load_dotenv
import oracledb

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
dsn = os.getenv("ORACLE_DSN")
wallet_password = os.getenv("ORACLE_WALLET_PASSWORD")
wallet_path_env = os.getenv("ORACLE_WALLET_PATH", "wallet")

wallet_dir = BASE_DIR / wallet_path_env

print("Usuario:", user)
print("DSN:", dsn)
print("Wallet path env:", wallet_path_env)
print("Ruta completa wallet:", wallet_dir)
print("Existe wallet:", wallet_dir.exists())
print("Existe tnsnames.ora:", (wallet_dir / "tnsnames.ora").exists())

if not wallet_dir.exists():
    raise Exception("La carpeta wallet no existe en la ruta indicada.")

if not (wallet_dir / "tnsnames.ora").exists():
    raise Exception("No se encontró tnsnames.ora dentro de la carpeta wallet.")

try:
    connection = oracledb.connect(
        user=user,
        password=password,
        dsn=dsn,
        config_dir=str(wallet_dir),
        wallet_location=str(wallet_dir),
        wallet_password=wallet_password
    )

    cursor = connection.cursor()
    cursor.execute("SELECT 'CONEXION EXITOSA A OCI' FROM dual")
    resultado = cursor.fetchone()

    print(resultado[0])

    cursor.close()
    connection.close()

except Exception as e:
    print("ERROR AL CONECTAR CON OCI:")
    print(e)