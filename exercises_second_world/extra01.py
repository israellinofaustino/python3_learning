# extract emails from text

import re

text = 'Contact us at contact@bol.com or give a feedback at feedback@bol.com'

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)

print(emails)
