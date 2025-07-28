import hashlib, json, sys

'''Helper function that provides a consistent way yo generate SHA 256
   hashes of various python data types. Ensures edges cases like python
   2 and 3 are handled'''
def Hash(msg=''):
    if type(msg) != str: #check type is not string
        msg = json.dumps(msg, sort_keys=True) #convert to json strings 
        # if we cant sort keys, cant guarantee repeatability 

    if sys.version_info.major == 2: #depending on the version of python
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
            #creates sha 256from msg and converts that byte string into unicode string
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
            #unicode is default in python 3 
