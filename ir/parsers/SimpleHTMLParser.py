from html.parser import HTMLParser


class SimpleHTMLParser(HTMLParser):
    content = ""

    def handle_data(self, data: str) -> None:
        self.content += data + " "

    @staticmethod
    def parse_html(data):
        parser = SimpleHTMLParser()
        parser.feed(data)
        return parser.content
