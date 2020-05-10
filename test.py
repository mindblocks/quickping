
from quickping import Quickping

test = Quickping("192.168.0.0", "192.168.0.128", log=True, threads=512)
test.active()
print(test.activeAddresses)

