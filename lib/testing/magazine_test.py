from author import Author
from magazine import Magazine
from article import Article

def test_top_publisher():
    # reset class variables before running
    Author.all = []
    Magazine.all = []
    Article.all = []

    a = Author("Alice")
    m1 = Magazine("TechMag", "Technology")
    m2 = Magazine("HealthNow", "Health")

    Article(a, m1, "AI Revolution in 2025")
    Article(a, m1, "Quantum Computing")
    Article(a, m2, "Healthy Living")

    assert Magazine.top_publisher() == m1
