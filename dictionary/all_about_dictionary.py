def dictionary():
    """
    A dictionary is a collection which is unordered, changeable and indexed
    The item stored in dictionary is in the form of key-value pair.
    Inorder to retrieve a data from the dictionary , we need to write dictionary[key].
    In an array, the indexes are integers. In dictionary, the indexes can be any type.
    """
    pass


def creating_dictionary():
    """
    Creating Dictionary to python.
    1.  my_dict = dict()-> using dict() constructor TC= O(1) SC=O(1)
    2.  my_dict = {} -> using {} TC= O(1) SC=O(1)

    for creating dictionary with key-value pair
    1.  my_dict = dict(key1='value1',key2='value2',key3='value3') TC =O(n) SC=O(n)
    2.  my_dict = {'key':'value1','key2':'value2','key3':'value3'} TC =O(n) SC=O(n)

    creating dictionary using tuples
    list_of_tuples = [('key1','value'),('key2','value2'),('key3','value3')] TC =O(n) SC=O(n)
    my_dict = dict(list_of_tuples)
    """
    my_dict = dict()
    print(my_dict)
    my_dict2 = {}
    print(my_dict2)
    eng_span = dict(one='uno', two='dos', three='tres')
    print(eng_span)
    eng_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    print(eng_sp)
    list_of_tuples = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
    my_dict3 = dict(list_of_tuples)
    print(my_dict3)


def dictionary_in_memory():
    """
    Dictionaries are indexed by keys and can be seen as associative arrays. Python dictionary are implemented using hash tables.
    It's an array whose indexes are obtained using a hash function on the keys.
    A hash table is a way of doing key-value lookups. You store the values in an array and then use a hash function
    to find the index of the array cell that corresponds to your key-value pair.

    :return:
    """
    pass


def insert_update_dictionary():
    """
    Dictionaries are mutable. We can add items or change the value of the existing items using assignment operator.
    If the key is already present, the value gets updated. Otherwise, a new key-value pair is added to the dictionary.
    TC = O(1) SC=O(1) (amortized for adding key-value pair)
    :return:
    """
    my_dict = {'name': 'Edy', 'age': 26}
    my_dict['age'] = 27
    my_dict['sex'] = 'male'
    print(my_dict)


def traversing_dictionary(dict):
    """
    Using a dictionary in the for statement, it traverses the keys of dictionary. TC = O(n) SC=O(1)
    """
    for key in dict:
        print(key, dict[key])


def search_dictionary(dict, value):
    """
    Searching can be done by using linear search on a dictionary. TC =O(n) SC = O(1)
    """
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'value does not exist'


def delete_dictionary():
    """
    using del dict[key] TC = O(1) SC = O(1)
    using pop - dict.pop(key,default_value) TC = O(1) SC = O(1)
    using popitem - removes and returns the last inserted key-value in the dictionary - dict.popitem() TC=O(1) SC=O(1)
    using clear - removes all the key-value pairs in the dictionary dict.clear() TC = O(n)
    """

    pass


if __name__ == "__main__":
    # creating_dictionary()
    insert_update_dictionary()
    my_dict = {'name': 'Edy', 'age': 27, 'sex': 'male'}
    traversing_dictionary(my_dict)
