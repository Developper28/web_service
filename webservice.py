import getopt
import sys
import os
from server import Server
from http.server import HTTPServer


# Global Variable
hostname = "0.0.0.0"
port = 8080


def get_port_from_env():
    key = "WEBSERVICE_PORT"
    port_env = port

    try:
        value = os.getenv(key)
        if value:
            port_env = int(value)

    except Exception as e:
        print(e)

    return port_env


def get_port_from_args(args):
    port_arg = port

    try:
        opts, _ = getopt.getopt(args, "p:")
        for opt in opts:

            if opt[0] == "-p":
                port_arg = int(opt[1])

    except Exception as e:
        print(e)

    return port_arg



def init():
    global port

    # Try to get the port from the environment variables first
    port = get_port_from_env()

    # Overide the port if '-p' option is given
    port = get_port_from_args(sys.argv[1:])


def main():
    web_server = HTTPServer((hostname, port), Server)
    print("Server started http://{}:{}".format(hostname, port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server closed.")


if __name__ == "__main__":
    init()
    main()
