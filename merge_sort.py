
class MergeSort:

    def __merge(self, list_to_sort, start, mid, end):
        left_list_size = mid - start + 1
        right_list_size = end - mid

        left_list = []
        for i in range(0, left_list_size):
            left_list.append(list_to_sort[start + i])
        left_list.append(float('inf'))

        right_list = []
        for i in range(0, right_list_size):
            right_list.append(list_to_sort[mid + i + 1])
        right_list.append(float('inf'))

        # import pdb; pdb.set_trace()
        i = 0
        j = 0
        k = start
        while k <= end:
            if left_list[i] <= right_list[j]:
                list_to_sort[k] = left_list[i]
                i += 1
            else:
                list_to_sort[k] = right_list[j]
                j += 1
            k += 1

    def __merge_sort(self, list_to_sort, start, end):
        if start < end:
            mid = (start+end) / 2
            # print mid
            self.__merge_sort(list_to_sort, start, mid)
            self.__merge_sort(list_to_sort, mid + 1, end)

            self.__merge(list_to_sort, start, mid, end)

    def sort(self, list_to_sort):
        self.__merge_sort(list_to_sort, 0, len(list_to_sort) - 1)
