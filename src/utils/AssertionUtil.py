# This class contains all method related to assertion and printing logs


def assert_equal(val1, val2,msg=None):
    """
    This method verifies if both the values are equal
    :param val1: input1
    :param val2: input2
    :return: none
    """
    if val1 == val2:
        print('Both values are equal')
    elif msg == None:
        assert False,"Both values are not same " +str(val1)+"  2nd val "+str(val2)
    else :
        assert False,msg +" 1st val : "+str(val1)+"  2nd val: "+str(val2)

def assert_not_equal(val1, val2):
    """
    This method verifies if both the values are equal
    :param val1: input1
    :param val2: input2
    :return: none
    """
    if val1 != val2:
        print('Both values are different')
    else:
        assert False,"Both values are same" +str(val1)+"  2nd val "+str(val2)


def assert_mandatory(response, mandatory, optional):
    if mandatory == set(set(response) - set(optional)):
        print(" Is Present")
    else:
        assert False, "Is not Present"


def assert_contains(expected_val, collection_val):
    """
    This method verifies expected_val is present in collection_val
    :param expected_val: val which need to be present in collection
    :param collection_val: collection of values
    :return: none
    """
    if expected_val in collection_val:
        print(expected_val + " Is Present")
    else:
        assert False,expected_val +" Is not Present"

def assert_not_contains(expected_val, collection_val):
    """
    This method verifies expected_val is present in collection_val
    :param expected_val: val which need to be present in collection
    :param collection_val: collection of values
    :return: none
    """
    if expected_val not in collection_val:
        print(expected_val + " Is not Present")
    else:
        assert False,expected_val +" Is Present"

def assert_condition(condition,val1,val2):
    """
    This method verifies the condition specified hold true
    :param condition: condition to verify
    :param val1: value
    :param val2: value
    :return: none
    """
    if condition(val1,val2):
        print(str(val1)+" "+str(condition)+" "+str(val2))
    else:
        assert False,"Expected Condition Not Satisfied "
