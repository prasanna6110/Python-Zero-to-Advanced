# 066 · pytest and doctest — Example 3: Fixtures and parametrize (pytest file content)
# Run: python example_3.py

# This shows a real pytest file. Running this example writes it out
# and runs it with pytest if pytest is installed.
import pathlib, subprocess, sys, importlib.util

TEST_CODE = '''
import pytest

@pytest.fixture
def inventory():
    return {"apple": 5, "mango": 0}

def test_in_stock(inventory):
    assert inventory["apple"] > 0

@pytest.mark.parametrize("word,expected", [("level", True), ("hello", False), ("", True)])
def test_palindrome(word, expected):
    assert (word == word[::-1]) is expected
'''
path = pathlib.Path("test_demo_pytest.py")
path.write_text(TEST_CODE)
if importlib.util.find_spec("pytest"):
    subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(path)])
else:
    print("pytest not installed. Run: pip install pytest")
    print(TEST_CODE)
path.unlink()
