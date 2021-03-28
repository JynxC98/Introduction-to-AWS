class ReadArticles:

    def __init__(self):
        self.dataPath = '/Users/harsh/Desktop/AWS/Docs/Article 1.rtf'

    def loadArticles(self,path):
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text
readObj = ReadArticles()
articleText=readObj.loadArticles()
print(articleText)