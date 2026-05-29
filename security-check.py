import os
import re

patrones = [
    r"password\s*=",
    r"api_key\s*=",
    r"secret\s*=",
]

archivos_revisados = 0

for raiz, _, archivos in os.walk("."):
    if ".git" in raiz:
        continue

    for archivo in archivos:
        if archivo.endswith((".py", ".js", ".txt", ".env")):
            ruta = os.path.join(raiz, archivo)
            archivos_revisados += 1

            with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                contenido = f.read()

            for patron in patrones:
                if re.search(patron, contenido, re.IGNORECASE):
                    print(f"Posible credencial encontrada en {ruta}")
                    exit(1)

print(f"Archivos revisados: {archivos_revisados}")
print("No se encontraron credenciales expuestas")
