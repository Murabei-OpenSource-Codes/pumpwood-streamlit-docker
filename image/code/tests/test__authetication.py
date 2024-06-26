"""Test Calendar DataBase API."""
import requests
import unittest
import pandas as pd
from pumpwood_communication.microservices import PumpWoodMicroService
from pumpwood_communication.exceptions import PumpWoodObjectDoesNotExist


microservice_test = PumpWoodMicroService(
    name="test", server_url="http://0.0.0.0:8080/")
auth_header = {
    'Authorization': 'Token 97325bbfc9606a41099ae077851ee693078ac31de4d3533e8093c9bc6300b0af'}
auth_cookie = {
    'PumpwoodAuthorization': 'Token 97325bbfc9606a41099ae077851ee693078ac31de4d3533e8093c9bc6300b0af'}
path_test_files = "etljob/tests/test_files/%s"


class TestDashboardAuthenticationApi(unittest.TestCase):
    load_balancer_address = "http://0.0.0.0:8080/"
    'Ip of the load balancer'
    apps_to_regenerate = []
    'Name of the apps to be regenerated after the test is over'

    test_address = "http://0.0.0.0:5000/"

    def setUp(self, *args, **kwargs):
        """Regen the database in the setUp calling reload end-point."""
        ######################
        # Regenerate database#
        for app in self.apps_to_regenerate:
            path = 'reload-db/' + app + '/'
            response = requests.get(self.load_balancer_address + path)
            if response.status_code != 200:
                raise Exception(app + ' regenerate: ', response.text)

    def test_server_is_up_and_running(self):
        response = self.session.get(
            self.load_balancer_address +
            'health-check/pumpwood-datalake-app/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'true')

    def test_check_logged(self):
        result = microservice_test.check_if_logged(auth_header)
        self.assertTrue(result)

    def test_check_logged_error(self):
        result = microservice_test.check_if_logged(auth_header={
            "Authorization": "Token esse-token-esta-errado"})
        self.assertFalse(result)
