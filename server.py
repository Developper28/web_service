from http.server import BaseHTTPRequestHandler
from datetime import datetime
import re
import subprocess
import json


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        processed_path = Server.process_query_path(self.path)
        endpoint = processed_path["root_path"]
        params = processed_path["params"]
        if endpoint == "/helloworld":
            name_str = "HelloStranger"
            if params:
                for param in params:
                    if param["key"] == "name":
                        name_str = param["value"]

            message = " ".join(re.findall("[A-Z][^A-Z]*", name_str))
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(message.encode(encoding="utf-8"))

        elif endpoint == "/versionz":
            git_hash = Server.execute_cmd("git rev-parse HEAD")
            project_path = Server.execute_cmd("pwd")
            project_name = project_path.split("/")[-1]
            data = {"project_name": project_name, "git_hash": git_hash}
            json_str = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_str.encode(encoding="utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Content not found".encode(encoding="utf-8"))

    def log_message(self, format, *args):
        date_str = self.log_date_time_string()
        date_object = datetime.strptime(date_str, "%d/%b/%Y %H:%M:%S")
        iso_date = date_object.isoformat()
        http_status = args[1]
        request = args[0]
        print("{} - {} - {}".format(iso_date, http_status, request))

    @staticmethod
    def process_query_path(url_path):
        # /helloworld?name=AlfredENeumann
        array_split = url_path.split("?")
        root_path = array_split[0]
        ans = {"root_path": root_path, "params": []}
        if len(array_split) == 2:
            params_str = array_split[1]
            params_list = params_str.split("&")
            for param in params_list:
                key, value = param.split("=")
                ans["params"].append({"key": key, "value": value})
        return ans

    @staticmethod
    def execute_cmd(cmd):
        ans = ""
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) as sbrs:
            subprocess_return = sbrs.stdout.read()
            subprocess_return = subprocess_return.decode("utf-8")
            sbrs.terminate()
            sbrs.wait()
            ans = subprocess_return[:-1]  # To remove /n

        return ans
