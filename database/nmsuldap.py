import ldap3
import getpass

def authenticate(u, p):
    server = ldap3.Server("ldaps://directory.nmsu.edu", 636, True)
    namefilter = "CN=" + u
    locationfilter = "OU=Banner Users,OU=Accounts,DC=acn,DC=ad,DC=nmsu,DC=edu"
    connection = ldap3.Connection(server, namefilter + "," + locationfilter, p)
    connection.bind()
    if(connection.search(locationfilter, "(sAMAccountName=" + u + ")")):
        return True
    return False

# username = input("Username: ")
# password = getpass.getpass()

# if (authenticate(username, password)):
#     print("You successfully validated your NMSU credentials.")
# else:
#     print("Your input credentials are not NMSU credentials.")