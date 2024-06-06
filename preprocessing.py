from dummyhtmldata import html
from bs4 import BeautifulSoup, Comment
import pprint
import re
import tiktoken as tiktoken
import logging
import pprint
import logging

def remove_script_style(soup):
    for script in soup.select('script'):
        script.extract()

    for script in soup.select('style'):
        script.extract()

    return soup

def remove_svg_elements(soup):
    for svg in soup.select('svg'):
        svg.extract()
    return soup

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    soup = remove_svg_elements(soup)
    soup = remove_script_style(soup)

    soup_str = str(soup)
    print("Cleaned HTML:")
    return soup_str


def split_string(input):
    length_to_split =4000 
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    num_tokens = len(encoding.encode(input))
    tokens = list(encoding.encode(input))
    substrings = []
    while tokens:
            if len(tokens) <= length_to_split:
                substrings.append(encoding.decode(tokens))
                break
            else:
                substrings.append(encoding.decode(tokens[:length_to_split]))
                tokens = tokens[length_to_split:]
    logging.info("substrings: %d", len(substrings))
    logging.info("substrings Generated")
    print("Substrings Generated")
    return substrings

def extract_json_code(text):
    code_block_pattern = re.compile(r'```json\n(.*?)\n```', re.DOTALL)
    code_blocks = code_block_pattern.findall(text)
    if code_blocks:
        return code_blocks[0]
    return None


# logging.basicConfig(level=logging.INFO, filename='output.log', filemode='w')
# logging.info(pprint.pformat(split_string(clean_html(html))))



