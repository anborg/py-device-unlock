import sys
def isUrlAccessible(url):

    try:
        import requests
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        if response:
            return True
    except Exception as e:
        sys.stderr.write("SOAP1 Service not reachable : {}\n".format(str(e)) )
        exit(1)
