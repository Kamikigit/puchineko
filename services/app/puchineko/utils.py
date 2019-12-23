

def text2link(text, entities):
    for url_info in entities['urls']:
        marked_up_url = f'<a href=\"{url_info["expanded_url"]}\">{url_info["expanded_url"]}</a>'
        text = text[:url_info["indices"][0]] + marked_up_url + text[url_info["indices"][1]:]

    if 'media' in entities:
        for media_info in entities['media']:
            marked_up_url = f'<img src=\"{media_info["media_url"]}\" alt=\"photo:{media_info["display_url"]}\" width=\"250px\" height=\"250px\">'
            text = text[:media_info['indices'][0]] + text[media_info['indices'][1]:] + "<br>" + marked_up_url
    
    return text