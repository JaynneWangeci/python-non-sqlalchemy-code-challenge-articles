import pytest
from author import Author
from magazine import Magazine
from article import Article

def test_article_has_title():
    a = Author("Alice")
    m = Magazine("TechMag", "Technology")
    art = Article(a, m, "AI Revolution in 2025")
    assert art.title == "AI Revolution in 2025"

def test_article_title_is_read_only():
    a = Author("Alice")
    m = Magazine("TechMag", "Technology")
    art = Article(a, m, "AI Revolution in 2025")
    with pytest.raises(AttributeError):
        art.title = "New Title"

def test_article_author_and_magazine():
    a = Author("Alice")
    m = Magazine("TechMag", "Technology")
    art = Article(a, m, "AI Revolution in 2025")
    assert art.author == a
    assert art.magazine == m

def test_article_can_change_author_and_magazine():
    a1 = Author("Alice")
    a2 = Author("Bob")
    m1 = Magazine("TechMag", "Technology")
    m2 = Magazine("HealthNow", "Health")
    art = Article(a1, m1, "AI Revolution in 2025")
    art.author = a2
    art.magazine = m2
    assert art.author == a2
    assert art.magazine == m2
