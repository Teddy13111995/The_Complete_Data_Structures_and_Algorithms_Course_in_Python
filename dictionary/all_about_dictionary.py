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


def dictionary_methods():
    """
    dict.clear() - delete all elements of dictionary, returns None
    dict.copy() - creates a copy of the dictionary, doesn't modify original one.
    dictionary.fromkeys(sequence[],value(default = None)) - creates a new dictionary from given sequence of elements with value provided by the user.
    dictionary.get(key,value(optional)) - returns value for specified key if the key is in the dictionary.
    dictionary.items() - a view object that displays a list of dictionaries, key-value tuple pairs.
    dictionary.keys() - returns a view object that returns the list of all keys in the dictionary.
    dictionary.popitem() - returns an arbitrary(last) element pair from the dictionary and removes that arbitrary element.
    dictionary.setdefault(key,default_value) - returns the value of the key if the key is in the dictionary, if not it inserts key with a value to the dictionary.
    dictionary.pop(key,default_value(when key is not in the dictionary)) - remove the key if key is in dictionary else returns default_value.
    dictionary.values() - returns a view object of the list of values present in the dictionary.
    dictionary.update(other_dictionary) - updates the dictionary with the elements from another dictionary object or from iterables of key-value pair.
                            If the key is in the dictionary, then it updates the value with new value.
    """
    pass


def dictionary_operations():
    """
    in/not in - check if key is in dictionary or value in dictionary.values().
    len() - count number of pairs in the dictionary.
    all() - checks if all keys are Ture(non-zeros) or False(0)
    any() - 1. if all values are tue - True 2. All values are False - False 3. If one value is True - True
    sorted() - return list of sorted keys.
    """
    pass


def dictionary_vs_list():
    """
    Dictionary                              List
    Unordered/ordered as of python 3.7      Ordered
    Access via keys                         Access via index
    Collection of key-value pair            Collection of elements
    Preferred when you have unique keys     Preferred when you have ordered data
    No duplicate members                    Allow duplicate members
    """
    pass


def dictionary_comprehension():
    """
    new_dict = {new_key:new_value for item in list}
    new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

    def count_word_frequency(words):
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

    def merge_dicts(dict1, dict2):
        result = dict1.copy()
        for key, value in dict2.items():
            result[key] = result.get(key, 0) + value
        return result

    def max_value_key(my_dict):
        return max(my_dict, key=my_dict.get)

    def reverse_dict(my_dict):
        return {v: k for k, v in my_dict.items()}


    """
    pass


if __name__ == "__main__":
    # creating_dictionary()
    insert_update_dictionary()
    my_dict = {'name': 'Edy', 'age': 27, 'sex': 'male'}
    traversing_dictionary(my_dict)
