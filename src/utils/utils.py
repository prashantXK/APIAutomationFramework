#read data from excel file
#read data from csv,json file

#JSON HEADERS-----

class Utils(object):

    def common_headers_json(self):
        headers= {
            "Content-Type" : "application/json"
        }
        return headers

#XML HEADERS-----

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/json"
        }

        return headers


#COOKIE HEADERS-----

def common_header_put_delete_patch_cookie(self,token):
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : "token" +str(token)
    }
    return headers

#BASIC_AUTH HEADERS-----


def common_header_put_patch_delete_basic_auth(self,basic_auth_value):
        headers = {
            "Content-Type" : "application/json",
            "Authorization" : "Basic" + str(basic_auth_value)
        }
        return headers








