from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

contents = doc.select('.heading-primary')[0].contents[0].strip()

print(contents)

more_contents = doc.select('.heading-25-extrabold.color-black')

for item in more_contents:
    print(item.contents[0].strip())

tag_name = doc.select('.heading-25-extrabold.color-black')[0].name
print(tag_name)

attrs = doc.select('.heading-25-extrabold.color-black')[0].attrs
print(attrs)

even_more_contents = doc.select('.heading-50-black.color-black')[0]

for child in even_more_contents.children:
    print(child)

# Note for Flatiron: You may want to be more explicit here about how to call `.strip` on the contents. "If we add .strip to the end" could make someone think they can just add `.strip` to the end of the `doc.select` query, but .strip can't be called on the list object that query returns, it needs to be called on the text itself. In this instance where there's only 1 item in the array, you could specify contents[0].strip() and this would achieve the desired result. If there were more than one item in the array, you'd need to iterate through each item to transform it.