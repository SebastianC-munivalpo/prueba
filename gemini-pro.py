import os
import google.generativeai as genai
import argparse

# 1. Configuración
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")

genai.configure(api_key=api_key)

# 2. Intentamos usar la versión específica '001' que es la más estable
nombre_modelo = 'gemini-1.5-flash-001'

try:
    # Configurar argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, required=True)
    args = parser.parse_args()

    # Intentar generar
    model = genai.GenerativeModel(nombre_modelo)
    response = model.generate_content(args.prompt)
    
    print("--- RESPUESTA DE GEMINI ---")
    print(response.text)
    print("---------------------------")

except Exception as e:
    print(f"❌ Error al usar el modelo '{nombre_modelo}': {e}")
    
    # 3. SI FALLA, LISTAR LOS MODELOS QUE SÍ FUNCIONAN
    print("\n🔍 BUSCANDO MODELOS DISPONIBLES EN TU CUENTA...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
    except Exception as list_error:
        print(f"No se pudieron listar los modelos: {list_error}")