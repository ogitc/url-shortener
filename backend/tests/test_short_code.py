import sys
from pathlib import Path

from app.short_code import generate_short_code

backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))


def test_generate_short_code_basic():
    c = generate_short_code(7)
    assert len(c) == 7
    assert c.isalnum()
