import os
import subprocess

"""
This module has helper methods to interact with phantomjs.
phantomjs must be on the executable path for this to work.
"""

def netsniff(url):
    """
    Uses netsniff.js from phantomjs examples folder to call
    a website and return http responses in json format.

    :param url:The url to be called
    :return: json object with responses
    """
    stdout = None
    #netsniff.js path
    file_path = os.path.dirname(os.path.realpath(__file__))
    netsniff_path = file_path+'/scripts/netsniff.js'
    if (os.path.isfile(netsniff_path)):
        try:
            proc = subprocess.Popen(["phantomjs", netsniff_path, url],stdout=subprocess.PIPE)
            stdout = proc.stdout.read().decode("utf-8")
        except FileNotFoundError:
            raise FileNotFoundError("phantomjs was not found in path")
        except:
            raise Exception("error executing netstiff for "+url)
    else:
        raise FileNotFoundError('scripts/netsniff.js not found')
    #Check to see if stdout returned error
    if "FAIL to load the address" in stdout:
        raise Exception("FAIL to load the address "+url)
    return stdout
