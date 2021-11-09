import re


def parse(markdown):
    lines = [headers(emphasis(line)) for line in markdown.splitlines()]
    lines = "".join(lines)
    if re.match("(.*)<li>(.*)", lines):
        start_index = lines.index("<li>")
        end_index = lines.rindex("</li>")
        return f"{lines[:start_index]}<ul>{lines[start_index:end_index + 5]}</ul>{lines[end_index + 5:]}"
    else:
        return lines


def emphasis(markdown):
    if re.match(r"(.*)__(.*)__(.*)", markdown):
        start_index = markdown.index("__")
        end_index = markdown.rindex("__")
        markdown = f"{markdown[:start_index]}<strong>{markdown[start_index + 2:end_index]}</strong>{markdown[end_index + 2:]}"
    if re.match(r"(.*)_(.*)_(.*)", markdown):
        start_index = markdown.index("_")
        end_index = markdown.rindex("_")
        markdown = f"{markdown[:start_index]}<em>{markdown[start_index + 1:end_index]}</em>{markdown[end_index + 1:]}"
    return markdown


def headers(markdown):
    if re.match("###### (.*)", markdown):
        markdown = f"<h6>{markdown[7:]}</h6>"
    elif re.match("## (.*)", markdown):
        markdown = f"<h2>{markdown[3:]}</h2>"
    elif re.match("# (.*)", markdown):
        markdown = f"<h1>{markdown[2:]}</h1>"
    else:
        markdown = lists(markdown)
    return markdown


def lists(markdown):
    if re.match(r"\* (.*)", markdown):
        markdown = f"<li>{markdown[2:]}</li>"
    else:
        markdown = f"<p>{markdown}</p>"
    return markdown
