import argparse

__author__ = "hamdielhamdi@outlook.com"
__date__ = "03/03/2021"


"""
probleme assumption :  https://en.wikipedia.org/wiki/Maximum_subarray_problem

the probleme describe in wikipidia docs is a one dim array, so we will take the same concept and 
extend it.

solution idea : the maximum sum subarray problem is the task of finding a contiguous 
subarray with the largest sum, within a given two-dimensional array A[1...n, 1...m] of numbers. 

time complexity  : k * O(n*m) where  n is nbr rows , m is the nbr of columns and k the nbr of 
time we pass thru the matrix (we repeat the loop in ). but since k is a cst so it's an O(n*m).
"""

class SubSquarFinder:
	# get matrix dim
	def get_dim(self, map):
		self.map = map
		# used to get matrix dim
		return  len(self.map), len(self.map[0])


	def storage(self, rows, colmuns):
		# create an empty vector
		# it will be used to store path 
		return [[0 for column in range(colmuns)] for row in range(rows)]
    
	def convert_to_binary(self, map):
		# this is used to convert the map to a binary map [0,1]
		# since 
		return [[1 if j == '.' else 0 for j in i  ] for i in map.split()]

	def create_path_history(self,row,col , store):   
		# iter thru row and col 
	    for index_row in range(0, row):  
	        for index_col in range(0, col):
	        	# check if not obstacle 
	            if (self.map[index_row][index_col] == 1):
	            	# check cif first cell  
	                if index_row == 0 or index_col == 0: 
	                	# get the min 
	                    store[index_row][index_col] = min(self.map[index_row][index_col], 1) 
	                else: 
	                    store[index_row][index_col] = min(store[index_row][index_col-1], store[index_row-1][index_col],store[index_row-1][index_col-1]) + 1
	            else: 
	                store[index_row][index_col] = 0
	    return store

	def maximize(self, store, row, col):
		max1 = max2 = 0
		init = store[0][0]
		for i in range(row):  
			for j in range(col):  
				if init < store[i][j]:  
					init = store[i][j]  
					max1 = i  
					max2 = j  
		return max1, max2,init 

	def render_result(self, max1, max2, init):
	    for index in range(max1, max1 - init, - 1):  
	        for row in range(max2, max2 - init, - 1):  
	        	self.map[index][row] = "x"
	    return self.map

	def reverse_process(self,row, col):
		for i in range(row):  
			for j in range(col):  
			    if  self.map[i][j] == 1 :
			        		self.map[i][j] = "."
			    if  self.map[i][j] == 0 :
			        		self.map[i][j] = "o"
		# last reformat
		output = ["".join(i) for i in self.map]
		print("\n".join(output))
			
		

def work_flow(map) : 
	# create an instance of sub square finder
	mp = SubSquarFinder()
	# conevrt map from .o --> 01
	map = mp.convert_to_binary(map)
	# get map dim 
	row, col = mp.get_dim(map)
	# create and store initial empty map 
	store = mp.storage(row, col)
	#
	mp.create_path_history(row, col, store)
	# Find a contiguous subarray with the largest sum
	max1, max2,init  = mp.maximize(store, row, col)
	mp.render_result(max1, max2,init )
	# conevrt map from 01 --> .0x
	mp.reverse_process(row, col)

# used to read files 
def read_file(path):
	with open(path, 'r') as f:
		return f.read()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='### subsquare finder ###')
	parser.add_argument('--input', metavar='N', type=str,
	                    help='input file path, can be one or many and most be separeted be blank space : eg  : -- input first_file.txt second_file.txt')
	args = parser.parse_args()
	
	input = args.input 

	print("--> Start programme.")
	
	for input_val in input.split(','):
		print(f'\nProcessing  : {input_val}')
	
		try : 
			map = read_file(input_val)
			work_flow(map)
		except Exception as e:
			print("--> map error !!! \n")
	