class Article:

    '''Defines class objects'''
    def __init__(self,title, description,url, urlToImage, content, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt




class Source:
    def __init__(self,id,name, description, language, country, url):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.country = country
        self.url = url