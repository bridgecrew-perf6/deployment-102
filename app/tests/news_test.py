import unittest
from app.models import Article

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_news_article = Article('Covid-19 Case arise','More people diagonised with covid-19', 'https://www.cbc.ca/news/canada/newfoundland-labrador/apocalypse-then-wave-prediction-1.6435963','https://i.cbc.ca/1.5471199.1582299129!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/crashing-waves-at-st-shott-s.jpg','This column is an instalment in our series Apocalypse Then\r\n, in which cultural historian Ainsley Hawthorn examines the issues of COVID-19 through the lens of the past. \r\nSince the beginning of the C… [+5646 chars]','2022-05-01T14:25:59Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article, Article ))
        
