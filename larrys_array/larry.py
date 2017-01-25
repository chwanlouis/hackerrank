# Enter your code here. Read input from STDIN. Print output to STDOUT


class LarrysArray(object):

	def __init__(self, array):
		self.array = array
		# print self.seek_lowest_value_unsorted(self.array)
		# print self.seek_highest_value_sorted(self.array)

	def robot_rotates(self, sub_array):
		sub_array.append(sub_array.pop(0))
		return sub_array

	def array_split(self, array, index):
		if index + 3 > len(array):
			return None, None, None
		head = array[:index]
		subset = array[index:index+3]
		tail = array[index+3:]
		return head, subset, tail

	def robot_operation(self, array, index):
		head, subset, tail = self.array_split(array, index)
		subset = self.robot_rotates(subset)
		return head + subset + tail

	def seek_lowest_value_unsorted(self, array):
		unsorted = list()
		for i in range(len(array)):
			if i+1 != array[i]:
				unsorted.append(array[i])
		return min(unsorted)

	def seek_highest_value_sorted(self, array):
		sorted_value = None
		for i in range(len(array)):
			if i+1 == array[i]:
				sorted_value = array[i]
			else:
				break
		return sorted_value

	def get_robot_acting_index(self, array):
		highest_sorted = self.seek_highest_value_sorted(array)
		lowest_unsorted = self.seek_lowest_value_unsorted(array)
		if highest_sorted is not None:
			unsorted_position = array.index(lowest_unsorted)
			sorted_position = array.index(highest_sorted)
			index = unsorted_position
			if unsorted_position - sorted_position == 2:
				index -= 1
			else:
				index -= 2
			return index
		else:
			return array.index(lowest_unsorted) - 1

	def get_tail_permutation_correct(self, array):
		highest_sorted = self.seek_highest_value_sorted(array)
		if highest_sorted > len(array) - 3:
			tail = array[-3:]
			sorted_tail = sorted(tail)
			for i in range(4):
				tail = self.robot_rotates(tail)
				if tail == sorted_tail:
					return True
			return False
		else:
			return True

	def sorting(self):
		while self.get_tail_permutation_correct(self.array):
			# print self.array
			index = self.get_robot_acting_index(self.array)
			self.array = self.robot_operation(self.array, index)
			if self.array == sorted(self.array):
				return True
		return False


class InputAdapter(onject):

	def __init__(self):
		self.number_of_test = int(raw_input())
		self.T = list()
		self.array = list()
		for i in range(self.number_of_test):
			T = int(raw_input())
			array = str(raw_input()).split(' ')
			self.T.append(T)
			array = [int(i) for i in array]
			self.array.append(array)
		for num_list in self.array:
			if self.can_sort(num_list):
				print 'YES'
			else:
				print 'NO'

	def can_sort(self, array):
		test = LarrysArray(array)
		return test.sorting()


if __name__ == '__main__':
	program = InputAdapter()