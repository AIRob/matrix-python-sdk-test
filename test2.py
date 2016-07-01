from matrix_client.api import MatrixHttpApi
import json
import re
import requests
import pprint
class MatrixError(Exception):
    """A generic Matrix error. Specific errors will subclass this."""
    pass

class MatrixUnexpectedResponse(MatrixError):
    """The home server gave an unexpected response. """
    def __init__(self, content=""):
        super(MatrixRequestError, self).__init__(content)
        self.content = content


class MatrixRequestError(MatrixError):
    """ The home server returned an error response. """

    def __init__(self, code=0, content=""):
        super(MatrixRequestError, self).__init__("%d: %s" % (code, content))
        self.code = code
        self.content = content

response = requests.request(
            "GET",
            "https://localhost:8448/_matrix/client/r0/sync",
            params = {"access_token":"MDAxN2xvY2F0aW9uIGxvY2FsaG9zdAowMDEzaWRlbnRpZmllciBrZXkKMDAxMGNpZCBnZW4gPSAxCjAwMjNjaWQgdXNlcl9pZCA9IEB3YXFlZTpsb2NhbGhvc3QKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMWRjaWQgdGltZSA8IDE0NjU2ODM0MzkzMzQKMDAyZnNpZ25hdHVyZSChe_RH_3PNOpgcerjdlXNRydkL_0LgjsJRPG-cJHg4sAo"},
            data =  json.dumps({}),
            headers = {"Content-Type" : "application/json"},
            verify = "/home/waqee/Desktop/matrix-python-sdk/localhost.tls.crt"
        )

if response.status_code < 200 or response.status_code >= 300:
    raise MatrixRequestError(
        code=response.status_code, content=response.text
    )
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())