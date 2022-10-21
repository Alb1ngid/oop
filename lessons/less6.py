import os
from envparse import env
print(os.environ.get('test_logit'))
env.read_envfile('options.env')
print(os.environ.get('PASSWORD'))