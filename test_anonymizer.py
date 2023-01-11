# Generating an anonymized ID from an 'Account ID'

import hashlib

account_id=float(4572) # '4572' is the Customer Account ID number
HASH_SALT="keij3ka2Hie2lilie1aiwab5oaQuooth"
salted_value = "{}{}".format(account_id, HASH_SALT) # combines the 'Customer Account ID number' with the 'HASH_SALT'

# Using the Hashlib function to create a random/anonymized account ID

anonymized_value=str(hashlib.sha1(salted_value.encode("utf-8")).hexdigest())[:12]
print (f"This is the 'Anonymized Account ID number': ", anonymized_value)

# print(anonymized_value)

#
# In order for the 'float' to work (line 5), use the 'Index Column' from the people-100.csv file