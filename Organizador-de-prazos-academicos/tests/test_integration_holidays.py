import pytest
from src.holidays_api import get_public_holidays

def test_get_public_holidays_returns_list():
    # Usa um país com dados públicos - BR
    data = get_public_holidays(2023, 'BR')
    assert isinstance(data, list)
    assert len(data) > 0
    item = data[0]
    assert 'date' in item and 'localName' in item and 'name' in item
