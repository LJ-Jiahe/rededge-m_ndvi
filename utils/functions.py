

def sort_key(content_name):
    content_name_split = content_name.split('.')[0].split('_')
    return int(content_name_split[1]) * 10 + int(content_name_split[2])