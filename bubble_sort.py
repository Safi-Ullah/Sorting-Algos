
class BubbleSort:

    def __swap(self, list_to_sort, i, j):
        temp = list_to_sort[i]
        list_to_sort[i] = list_to_sort[j]
        list_to_sort[j] = temp

    def sort(self, list_to_sort):
        for i in range(0,len(list_to_sort) - 1):
            flag = False

            for j in range(0, len(list_to_sort) - i - 1):
                if(list_to_sort[j] > list_to_sort[j + 1]):
                    self.__swap(list_to_sort, j, j + 1)
                    flag = True

            if flag == False:
                return
