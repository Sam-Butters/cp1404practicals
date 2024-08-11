import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

search_phrase = input('Enter a search phrase: ').strip()

while search_phrase != '':
    try:
        results = wikipedia.search(search_phrase)

        if not results:
            print("No pages found for the search phrase.")
        else:

            page_title = results[0]
            page = wikipedia.page(page_title)

            print(f'\n{page.title}')
            print(f'{page.summary[:200]}...')  # Print the first 200 characters of the summary
            print(page.url)

    except DisambiguationError as e:
        print(f'We need a more specific title. Try one of the following, or a new search:\n')
    except PageError:
        print('Page does not exist.')

    search_phrase = input('Enter a search phrase: ').strip()

print('Thank you.')
