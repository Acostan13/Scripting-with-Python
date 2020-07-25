import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res


def read_res(response):
    print(response.text)


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)
    print(hashes)


def pwned_api_check(password):
    # Check password if it exists in API response
    print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())  # 40BD001563085FC35165329EA1FF5C5ECBDBBEEF
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    print(response)
    return read_res(response), get_password_leaks_count(response, tail)


#request_api_data('123')
pwned_api_check('123')