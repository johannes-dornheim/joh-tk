from johtk.johpd import melt_cols
from johtk.data import cities

import pytest

def test_melt_cols():
    result = melt_cols(cities, ['population','country'])
    expected = {'total_len':14}
    assert len(result) == expected['total_len']
