import configparser
from passlib.hash import pbkdf2_sha512


odoo_config = 'odoo.conf'
# nimda is the new password
nimda_hash = pbkdf2_sha512.hash("nimda")
parser = configparser.RawConfigParser()
parser.read(odoo_config)

try:
    parser.set('options', 'admin_passwd', nimda_hash)
except configparser.NoSectionError:
    print('error opening the config file.')

with open(odoo_config, 'w') as configfile:
    parser.write(configfile)
