s = 'abc-xyz-123-789-ABC-XYZ'

print(s.replace('xyz', ''))
# abc--123-789-ABC-XYZ

import re

s = 'abc-xyz-123-789-ABC-XYZ'

print(re.sub('\d+', '', s))
# abc-xyz---ABC-XYZ
