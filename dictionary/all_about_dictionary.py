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
    my_dict2 = {}  #
    print(my_dict2)
    eng_span = dict(one='uno', two='dos', three='tres')
    print(eng_span)
    eng_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    print(eng_sp)
    list_of_tuples = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
    my_dict3 = dict(list_of_tuples)
    print(my_dict3)


if __name__ == "__main__":
    creating_dictionary()
