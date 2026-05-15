import requests

BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"

def get_public_holidays(year: int, country_code: str):
    """Busca feriados públicos pelo serviço Nager.Date.

    Exemplo de resposta: lista de objetos com keys 'date', 'localName', 'name', etc.
    """
    url = f"{BASE_URL}/{year}/{country_code}"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"API retornou status {resp.status_code}")
    data = resp.json()
    return data

if __name__ == '__main__':
    # exemplo rápido
    print(get_public_holidays(2024, 'BR'))
