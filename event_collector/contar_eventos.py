import json

def contar_eventos():
    try:
        with open('eventos.json', 'r', encoding='utf-8') as f:
            eventos = json.load(f)
            print(f"Total de eventos cargados: {len(eventos)}")
    except FileNotFoundError:
        print("error")

if __name__ == "__main__":
    contar_eventos()
