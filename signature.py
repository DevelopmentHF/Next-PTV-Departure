# Code modified from 'Serge' in the developer community
# Accessed via PTV-API signature creation document page 12

from hashlib import sha1
import hmac

def getURL(request):

    # Accessed via request email to APIKeyRequest@ptv.vic.gov.au
    devID = 3002243
    unencodedkey = 'e93e5fac-74de-42ca-ac1c-48ed2b1428e6'

    # Encode key for hash function to operate (also applied to `raw` inline)
    key = unencodedkey.encode('utf-8')

    # Generate correct request syntax
    request = request + ('&' if ('?' in request) else '?')
    raw = request+'devid={0}'.format(devID)

    # Generate hash signature
    hashed = hmac.new(key, raw.encode('utf-8'), sha1)
    signature = hashed.hexdigest()

    # Return correct URL
    return 'http://timetableapi.ptv.vic.gov.au'+raw+'&signature={1}'.format(devID, signature)



