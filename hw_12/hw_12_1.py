import re
import codecs
from typing import Optional


def delete_html_tags(html_file: str, result_file: Optional[str] = 'cleaned.txt') -> None:
    """
    Clean HTML tags from a file and write clean text to a new file.
    Removes empty lines and excess whitespace.

    Args:
        html_file (str): Path to input HTML file
        result_file (str): Path to output text file (default: 'cleaned.txt')
    """

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', '', html)

    # Remove empty lines and normalize whitespace
    lines = [line.strip() for line in clean_text.splitlines()]
    clean_lines = [line for line in lines if line]

    # Write cleaned text
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(clean_lines))


delete_html_tags("draft.html")
