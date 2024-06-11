from bs4 import BeautifulSoup, Comment
import re
import tiktoken as tiktoken

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
    """
    Cleans the given HTML by removing SVG elements, script tags, and style tags.

    Args:
        html (str): The HTML string to be cleaned.

    Returns:
        str: The cleaned HTML string.
    """
    soup = BeautifulSoup(html, "html.parser")
    soup = remove_svg_elements(soup)
    soup = remove_script_style(soup)

    soup_str = str(soup)
    print("Cleaned HTML:")
    return soup_str


def split_string(input):
    """
    Splits a given input string into substrings of maximum length of x tokens.

    Args:
        input (str): The input string to be split.

    Returns:
        list: A list of substrings generated from the input string.
    """
    length_to_split = 4000
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
    return substrings


def extract_json_code(text):
    """
    Extracts the JSON code from a given markdown Format

    Args:
        text (str): The text containing the JSON.

    Returns:
        str or None: The extracted JSON , or None if no json block is found.
    """
    code_block_pattern = re.compile(r'```json\n(.*?)\n```', re.DOTALL)
    code_blocks = code_block_pattern.findall(text)
    if code_blocks:
        return code_blocks[0]
    return None





