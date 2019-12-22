import re

def text2link(text, entities):
    for url_info in entities['urls']:
        marked_up_url = f'<a href=\"{url_info["url"]}\">{url_info["url"]}</a>'
        text = text[:url_info["indices"][0]] + marked_up_url + text[url_info["indices"][1]:]
    
    return text