import requests

BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"

def get_public_holidays(year: int, country_code: str):
    """Busca feriados públicos pelo serviço Nager.Date.

    Exemplo de resposta: lista de objetos com keys 'date', 'localName', 'name', etc.
    """
    url = f"{BASE_URL}/{year}/{country_code}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Falha ao acessar a API de feriados: {exc}") from exc

    return resp.json()

if __name__ == '__main__':
    # exemplo rápido
    print(get_public_holidays(2024, 'BR'))
