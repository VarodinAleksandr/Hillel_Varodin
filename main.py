from urllib import parse as p


def parse(query: str) -> dict:
    p.parse_qs(p.urlsplit(query).query)
    itog = dict(p.parse_qsl(p.urlsplit(query).query))
    print(itog)
    return itog


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&surname=Shevchecko') == {'name': 'ferret',
                                                                                                     'color': 'purple',
                                                                                                     'surname': 'Shevchecko'}
    assert parse("http://www.example.org/default.html?ct=32&op=92&item=98") == {'item': '98', 'op': '92', 'ct': '32'}
    assert parse("http://www.example.org/default.html?ct=32&op=92") == {'ct': '32', 'op': '92'}
    assert parse('http://example.com/?&') == {}
    assert parse('http://example.com/?&=name') == {'': 'name'}
    assert parse("https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&type=3&theater") == {
        'fbid': '2068026323275211', 'set': 'a.269104153167446', 'type': '3'}
    assert parse('http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument') == {
        'key1': 'value1', 'key2': 'value2'}
    assert parse('http:/mypage.html?one=1&two=2&three=3') == {'one': '1', 'two': '2', 'three': '3'}
    assert parse('https://example.com/store?page=10&limit=15&price=ASC') == {'page': '10', 'limit': '15',
                                                                             'price': 'ASC'}
    assert parse('http://127.0.0.1:8000/items/?skip=0&limit=10') == {'skip': '0', 'limit': '10'}
