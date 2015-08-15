import unittest





def parse_url(url):
    class UrlObject():
        def __init__(self, protocol):
            self.protocol = protocol
    if url[0] == 'h':
        return UrlObject('http')
    else:
        return UrlObject('ftp')


class test_basic_example(unittest.TestCase):
    def setUp(self):
        self.url_object = parse_url('http://www.site.com')


    def test_finds_correct_http_protocol(self):
        protocol = self.url_object.protocol
        self.assertEqual('http', protocol)

    def test_finds_correct_ftp_protocol(self):
        url_object = parse_url('ftp://www.site.com')
        protocol = url_object.protocol
        self.assertEqual('ftp', protocol)

    def test_finds_site(self):
