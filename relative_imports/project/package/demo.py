print('__file__={} | __name__={} | __package__={}'.format(__file__,__name__,str(__package__)))
from .. import config
print("The value of config.count is {0}".\
format(config.count))
