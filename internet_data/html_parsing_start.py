
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data: str) -> None:
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position: ", pos[1])
        return super().handle_comment(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position: ", pos[1])
        return super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position: ", pos[1])
        return super().handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if data.isspace():
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position: ", pos[1])
        return super().handle_data(data)

def main():
    parser = MyHTMLParser()
    f = open("htmlsample.html")
    if f.mode == "r":
        print("ok")
        contents = f.read()
        parser.feed(contents)
        parser.handle_comment(contents)

if __name__ == "__main__":
    main()