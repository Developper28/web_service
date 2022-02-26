from http.server import BaseHTTPRequestHandler, HTTPServer
import re


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        processed_path = Server.process_query_path(self.path)
        endpoint = processed_path["root_path"]
        params = processed_path["params"]
        print("Hello ", processed_path)
        if endpoint == "/helloworld":
            name_str = "HelloStranger"
            if params:
                for param in params:
                    if param["key"] == "name":
                        name_str = param["value"]

            message = " ".join(re.findall('[A-Z][^A-Z]*', name_str))
                    

        elif endpoint == "/versionz":
            message = "ToDo Git Hash"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf-8"))


    @staticmethod
    def process_query_path(url_path):
        #/helloworld?name=AlfredENeumann
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

# Global Variable
hostname = "localhost"
port = 8080

if __name__ == "__main__":        
    web_server = HTTPServer((hostname, port), Server)
    print("Server started http://{}:{}".format(hostname, port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server closed.")

