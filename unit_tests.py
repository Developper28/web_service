import os
import unittest
from server import Server
from webservice import get_port_from_args, get_port_from_env


class TestHelperMethod(unittest.TestCase):
    def test_port_env(self):
        default_port = 8080
        port_1 = 8081
        os.environ["WEBSERVICE_PORT"] = str(port_1)
        self.assertEqual(get_port_from_env(), port_1)

        port_2 = 5000
        os.environ["WEBSERVICE_PORT"] = str(port_2)
        self.assertEqual(get_port_from_env(), port_2)

        os.environ["WEBSERVICE_PORT"] = ""
        self.assertEqual(get_port_from_env(), default_port)

    def test_port_arg(self):
        default_port = 8080

        args_1 = ["-p", "5050"]
        expected_port_1 = 5050
        args_2 = ["-p", "5053"]
        expected_port_2 = 5053
        args_3 = ["-s", "5000"]
        expected_port_3 = default_port

        args_4 = ["-p"]
        expected_port_4 = default_port

        self.assertEqual(get_port_from_args(args_1), expected_port_1)
        self.assertEqual(get_port_from_args(args_2), expected_port_2)
        self.assertEqual(get_port_from_args(args_3), expected_port_3)
        self.assertEqual(get_port_from_args(args_4), expected_port_4)


class TestServerStaticMethods(unittest.TestCase):
    def test_process_query(self):
        path_1 = "/helloworld?name=AlfredENeumann"
        expected_ans_1 = {
            "root_path": "/helloworld",
            "params": [{"key": "name", "value": "AlfredENeumann"}],
        }
        path_2 = "/home?username=UserName1&passwd=password1"
        expected_ans_2 = {
            "root_path": "/home",
            "params": [
                {"key": "username", "value": "UserName1"},
                {"key": "passwd", "value": "password1"},
            ],
        }
        self.assertEqual(Server.process_query_path(path_1), expected_ans_1)
        self.assertEqual(Server.process_query_path(path_2), expected_ans_2)

    def test_execute_cmd(self):
        cmd_1 = "pwd"
        cmd_2 = "echo hello"
        expected_ans_1_end = "web_service"
        expected_ans_2 = "hello"
        self.assertTrue(Server.execute_cmd(cmd_1).endswith(expected_ans_1_end))
        self.assertEqual(Server.execute_cmd(cmd_2), expected_ans_2)


if __name__ == "__main__":
    unittest.main()
