from urllib import parse


def strip_params_from_url(url):
    return url.split("?")[0]


def add_params_to_url(url, params):
    url_parts = list(parse.urlparse(url))
    query = dict(parse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = parse.urlencode(query)
    return parse.urlunparse(url_parts)
