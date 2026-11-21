
import unittest
from recommendation import recommend_courses
from collaborative import recommend_for_student
from hybrid import hybrid_recommend


class RecommendationTests(unittest.TestCase):

    def test_content_based(self):
        result = recommend_courses(
            "Python programming",
            "Data Scientist"
        )
        self.assertFalse(result.empty)
        self.assertLessEqual(len(result), 5)

    def test_collaborative(self):
        result = recommend_for_student("S1")
        self.assertFalse(result.empty)

    def test_hybrid(self):
        result = hybrid_recommend(
            "Python programming data analysis",
            "Data Scientist",
            "S1"
        )
        self.assertFalse(result.empty)
        self.assertLessEqual(len(result), 5)


if __name__ == "__main__":
    unittest.main()
