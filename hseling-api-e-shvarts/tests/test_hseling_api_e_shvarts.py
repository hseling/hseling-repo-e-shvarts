import unittest

import hseling_api_e_shvarts


class HSELing_API_E_shvartsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_e_shvarts.app.test_client()

    def test_index(self):
        rv = self.app.get('/healthz')
        self.assertIn('Application e-shvArts', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
