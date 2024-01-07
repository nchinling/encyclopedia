from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display_income_statement():
    if request.method == 'POST':
        # Get ticker and statement_type from the submitted form
        search_entry = request.form.get('search_entry')
    else:
        search_entry = request.args.get(
            'search_entry', '')

    # Construct the URL based on the ticker and statement_type
    url = f"https://en.wikipedia.org/wiki/{search_entry}"
    # headers = {"User-Agent": "Chrome/117.0.5938.132"}
    # entry_result = requests.get(url, headers=headers)
    entry_result = requests.get(url)
    html_content = entry_result.text
    # page_content = page.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Create a dictionary to store the income statement
    title = soup.find(id="firstHeading")
    title_text = title.text

    image = soup.find()

    entry = soup.find(id="mw-content-text")
    image = entry.find('img')
    if image:
        # You can access attributes of the img tag, for example, the 'src' attribute
        img_src = image.get('src', 'No image source found')
        print(f"Image source: {img_src}")
    else:
        print("No img tag found within the entry element")

    if entry:
        p_tags_within_entry = entry.find_all('p')

        paragraph_texts = [p_tag.text for p_tag in p_tags_within_entry]

    return render_template('encyclopedia.html', title=title_text, entry=paragraph_texts, image=img_src)


if __name__ == '__main__':
    app.run()
