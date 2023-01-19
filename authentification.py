import ldap
 
if __name__ == "__main__":
  	ldap_server="127.0.0.1"
	username = "haythem"
	password= "haythem"
	# the following is the user_dn format provided by the ldap server
	user_dn = "uid="+username+",ou=someou,dc=somedc,dc=local"
	
	base_dn = "dc=insat,dc=local"
	connect = ldap.open(ldap_server)
	search_filter = "uid="+username
	try:
		#if authentication successful, get the full user data
		connect.bind_s(user_dn,password)
		result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
		# return all user data results
		connect.unbind_s()
		print (result)
	except ldap.LDAPError:
		connect.unbind_s()
		print ("authentication error")