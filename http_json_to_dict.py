import json
import httplib

def get_json(host, port, path, result):
    '''
    To to pull HTTP JSON data in to specified dict.
    Why not just return the dict?  This way it can be used as a thread (i.e. async).
    '''
    conn = httplib.HTTPConnection(host, port)
    conn.request('GET', path)
    resp = conn.getresponse()
    if resp.status != 200:
        raise "HTTP Error!"
    result.update(json.loads(resp.read()))


# Example:
results = {}
get_json('example.com', 80, '/json.php', results)
# or if threading
get_json_thread = threading.Thread(target=get_json,
    args=('example.com', 80, '/json.php', results))
