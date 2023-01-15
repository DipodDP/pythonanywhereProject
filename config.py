import sshtunnel

from getpass import getuser


# Database setup
# username = getuser()        # you may put your username instead
username = 'Dipod'        # you may put your username instead

password = "DBserv_24"  # use your MySQL password
# ssh_password = "servDP24"
hostname = f"{username}.mysql.eu.pythonanywhere-services.com"
# tunnel = sshtunnel.SSHTunnelForwarder(
#     'ssh.eu.pythonanywhere.com', ssh_username=username, ssh_password=ssh_password,
#     remote_bind_address=(f"{username}.mysql.eu.pythonanywhere-services.com", 3333)
# )
#
# tunnel.start()

# hostname = "127.0.0.1:{}".format(tunnel.local_bind_port)
databasename = f"{username}$asyncinweb"
SQLALCHEMY_DATABASE_URI = f'sqlite:///{username}.db'

# SQLALCHEMY_DATABASE_URI = (
#     f"mysql://{username}:{password}@{hostname}/{databasename}"
# )
# SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 299}
# SQLALCHEMY_TRACK_MODIFICATIONS = False
