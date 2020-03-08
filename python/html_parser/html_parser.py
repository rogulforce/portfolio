import requests
from urllib.request import urlopen
import re


class Stack:
    """
    prosta klasa stosu
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def html_obtain(file_or_page):
    """
    Funkcja mająca za zadanie wyciągnąć tekst z pliku lub strony pisanej w języku html
    :param file_or_page: plik .html, .txt lub strona
    :return content: zawartość strony w postaci stringa
    """
    if file_or_page[:8] == 'https://':
        # czytamy plik za pomocą 'requests'
        page = requests.get(file_or_page)
        content = str(page.content)
        return content
    elif file_or_page[-5:] == '.html':
        # czytamy plik za pomocą 'urlopen'
        file = "file:{}".format(file_or_page)
        content = str(urlopen(file).read())
        return content
    else:               # dla txt
        content = open(file_or_page, 'r').read()
        return content

def comment_destroyer(text):
    """
    Funkcja ma za zadanie usunąć komentarze z tekstu
    :param text: tekst w skłądni html
    :return: tekst w składni html
    """
    beggining_comment = []
    ending_comment = []

    for match in re.finditer(r'<!--', text):
        beggining_comment.append(match.span()[0])
    for match in re.finditer(r'-->', text):
        ending_comment.append(match.span()[1])
    comments = list(zip(beggining_comment, ending_comment))
    for comment in comments:
        text = text.replace(text[comment[0]:comment[1]], (comment[1]-comment[0])*' ')   # zamiana komentarzy na spacje
    return text


def tag_taker(text):
    """
    Funkcja mająca za zadanie wyciągnąć listę tagów z pliku w języku html
    :param text: tekst html
    :return tags: lista tagów
    """
    new_text = comment_destroyer(text)
    openings = [place + 1 for place, character in enumerate(new_text) if character == '<']
    closings = [place for place, character in enumerate(new_text) if character == '>']

    places = list(zip(openings, closings))
    pre_tags = []
    tags = []
    for place in places:
        pre_tags.append(new_text[place[0]:place[1]])
    for tag in pre_tags:    # wyrzucam samozamykające się tagi z \ i !doctype
        if tag[0] == '!' or tag[-1] == '/':
            new_text.replace(tag, '')
            pre_tags.remove(tag)
    for tag in pre_tags:    # wyrzucam odniesienia zostawiając sam tag
        splitted = tag.split()
        tags.append(splitted[0])
    auto_closing_tags = ['link', 'br', 'hr', 'img', 'meta', 'source']
    #wyrzucam samozamykające się tagi
    tags = [item for item in tags if item not in auto_closing_tags]
    return tags


def checking_HTML_correctness(file_or_page):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, bądź adres strony którą ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    print(f'checking for {file_or_page}')
    html_stack = Stack()
    html_text = html_obtain(file_or_page)

    tags = tag_taker(html_text)

    breaker = 0 # zeby moc przerwac funckje wewnatrz pętli
    for tag in tags:

        if tag[0] != '/':
            html_stack.push(tag)
            print(f'PUSH: {tag}')
        else:
            if tag[1:] == html_stack.items[-1]:
                html_stack.pop()
                print(f'POP: {tag[1:]}')
            else:
                print(f'ERROR! NO OPENING FOR "{tag}"')
                breaker = True
                break
    if breaker == 0:
        if len(html_stack.items) > 0:
            print(f'ERROR FOLLOWING TAGS: {html_stack.items} ARE NOT CLOSED!')
        else:
            print('IT SEEMS TO BE CORRECT...')
    print('\n\n')


if __name__ == "__main__":
    checking_HTML_correctness("sampleHTML_1.txt")
    checking_HTML_correctness("sampleHTML_2.txt")
    checking_HTML_correctness("sampleHTML_3.html")
    checking_HTML_correctness('https://jsos.pwr.edu.pl/')
