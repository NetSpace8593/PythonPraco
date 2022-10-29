def build_profile(first, last, age, **user_info):


    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    return user_info

	
