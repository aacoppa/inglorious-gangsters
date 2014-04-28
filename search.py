def find_schools(user, colleges):
    """
        Finds new potential schools for our student
    """
    reach_level = .4
    target_level = .6
    safety_level = .8

    targets = []
    safetys = []
    reachs = []
    user_level = user.get_level()
    for school in colleges:
        value = get_difficulty_comparison(user_level) 
        print school.find_location()
        if value < reach_level:
            reachs.append(school)
        elif value < target_level:
            safetys.append(school)
    ret['safetys'] = safetys
    ret['targets'] = targets
    ret['reachs'] = reachs
    return ret



from College import College
C = College("Yale University", None, None, None)
C.find_location()
