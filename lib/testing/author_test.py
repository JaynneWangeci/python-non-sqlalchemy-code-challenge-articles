import pytest
from author import Author
from magazine import Magazine
from article import Article

def test_author_has_name():
    a = Author("Alice")
    assert a.name == "Alice"

def test_author_name_is_read_only():
    a = Author("Alice")
    with pytest.raises(AttributeError):
        a.name = "Bob"

def test_author_articles():
    a = Author("Alice")
    m = Magazine("TechMag", "Technology")
    art = Article(a, m, "AI Revolution in 2025")
    assert art in a.articles()

def test_author_magazines():
    a = Author("Alice")
    m1 = Magazine("TechMag", "Technology")
    m2 = Magazine("HealthNow", "Health")
    Article(a, m1, "AI in 2025")
    Article(a, m2, "Healthy Habits Daily")
    assert m1 in a.magazines()
    assert m2 in a.magazines()

def test_add_article_creates_article():
    a = Author("Alice")
    m = Magazine("TechMag", "Technology")
    art = a.add_article(m, "New Innovations")
    assert isinstance(art, Article)
    assert art in a.articles()

def test_topic_areas():
    a = Author("Alice")
    m1 = Magazine("TechMag", "Technology")
    m2 = Magazine("HealthNow", "Health")
    a.add_article(m1, "AI in 2025")
    a.add_article(m2, "Healthy Habits")
    assert "Technology" in a.topic_areas()
    assert "Health" in a.topic_areas()
