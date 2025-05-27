import tempfile
from tasks import read_lines

def test_read_lines():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        f.write("Hello\nWorld\nPython\n")
        f.seek(0)
        lines = list(read_lines(f.name))
        assert lines == ["Hello\n", "World\n", "Python\n"]