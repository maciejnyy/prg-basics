required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", 'execute','full access'}

has_permissions = set(required_permissions).issubset(user_permissions)  # subset
print(has_permissions)  # Will return False because "execute" is missing.