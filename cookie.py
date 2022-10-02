from http.cookies import SimpleCookie


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {k: v.value for k, v in cookie.items()}
    print(cookies)
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;surname=igor;') == {'name': 'Dima=User', 'age': '28', 'surname': 'igor'}
    assert parse_cookie('name=bijaya; comment=Comment1; expires=Mon, 26-Jul-2021 06:34:02 GMT; path=/; '
                        'domain=.google.com; Secure; HttpOnly; SameSite=none; Max-Age=244114; Version=1.2; '
                        'priority=high;') == {'name': 'bijaya', 'priority': 'high'}
    assert parse_cookie('top=1;low=10;hight=5;') == {'top': '1', 'low': '10', 'hight': '5'}
    assert parse_cookie('color=green;name=uri;') == {'color': 'green', 'name': 'uri'}
    assert parse_cookie('keebler=E=mc2; L=Loves; fudge=012;') == {'keebler': 'E=mc2', 'L': 'Loves', 'fudge': '012'}
    assert parse_cookie('Customer="WILE_E_COYOTE"; Version=1; Path=/acme') == {'Customer': 'WILE_E_COYOTE'}
    assert parse_cookie('Customer="W"; expires=Wed, 01 Jan 2010 00:00:00 GMT') == {'Customer': 'W'}
    assert parse_cookie('long=last; otto="": limit;') == {'long': 'last'}
    assert parse_cookie('tanya=sasha; sasha=tanya; python=qwerty:') == {'tanya': 'sasha', 'sasha': 'tanya', 'python': 'qwerty:'}
    assert parse_cookie('atleast=its;final=horray; and=and:') == {'atleast': 'its', 'final': 'horray', 'and': 'and:'}
