from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()

    def error(self,message):
        pass

    def handle_startag(self,tag,attrs):
        if tag=='a':
            #loop through
            for(attribute,value)in attrs:
                if attribute=='href':
                    #join the incomplete found url with the base url
                    url=parse.urljoin(self.base_url,value)
                    #add the url to the set of urls that we have
                    self.links.add(url)

    def page_links(self):
        return self.links     