import pytest
from project.project import load_data, search_word, get_synonyms

@pytest.fixture
def sample_data():
    return [
        {"word": "happy", "definition": "...", "synonyms": ["joyful"]},
        {"word": "brave", "definition": "...", "synonyms": ["courageous"]}
    ]

def test_load_data():
    data = load_data()
    assert isinstance(data, list)

def test_search_word_found(sample_data):
    result = search_word(sample_data, "happy")
    assert result["word"] == "happy"

def test_search_word_not_found(sample_data):
    assert search_word(sample_data, "unknown") is None

def test_get_synonyms(sample_data):
    word = search_word(sample_data, "happy")
    assert "joyful" in get_synonyms(word)
