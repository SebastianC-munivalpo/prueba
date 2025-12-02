import os
import google.generativeai as genai
import argparse

# 1. Configurar la API Key desde las variables de entorno
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")

genai.configure(api_key=api_key)

# 2. Configurar el modelo
model = genai.GenerativeModel('gemini-1.5-flash-001')
# 3. Configurar argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Gemini CLI para GitHub Actions')
parser.add_argument('--prompt', type=str, required=True, help='El prompt para enviar a Gemini')

args = parser.parse_args()

# 4. Generar contenido
try:
    response = model.generate_content(args.prompt)
    print("--- RESPUESTA DE GEMINI ---")
    print(response.text)
    print("---------------------------")
except Exception as e:
    print(f"Error al conectar con Gemini: {e}")