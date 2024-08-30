"""
Conftest file.
"""

import pytest
from unittest.mock import patch


@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get
