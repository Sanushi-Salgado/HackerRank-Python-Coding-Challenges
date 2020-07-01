if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # numbers_list = list(arr)
    # maximum = max(numbers_list)
    #
    # for i in range(len(numbers_list)):
    #     if(numbers_list[i] == maximum):
    #         numbers_list.remove( numbers_list[i] )
    #
    # second_maximum = max(numbers_list)
    # print(second_maximum)

    # numbers_list = list(arr)
    maximum = max(arr)
    for i in range(len(arr)):
        if list(arr).pop()[i] > maximum :
            maximum = arr[i]

    print(maximum)