
from quickping import Quickping

test = Quickping("192.168.0.0", "192.168.0.128", ignore=["192.168.0.22"], threads=512, log=True)
test.active()

print(test.deactiveAddresses)
print(test.activeAddresses)

