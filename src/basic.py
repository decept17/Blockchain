import hashlib, json, sys
import random

random.seed(0) #initalizes the internal state and ensures its reproducabile

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

''' Function generate a simple balance token transfer between alice and bob ensuring the 
    total value of tokens remains constant but without considering individuals accounts '''
def makeTransaction(maxValue=3):
    #will create valid transactions in the range of (1,maxValue)
    sign = int(random.getrandbits(1))*2 - 1 #this will randomly choose -1 or 1
    amount = random.randint(1,maxValue)
    alicePays = sign * amount
    bobPays = -1 * alicePays

    return {'Alice':alicePays,'Bob':bobPays}
    #note that this has nothing to do with wether they have the amount to pay or not