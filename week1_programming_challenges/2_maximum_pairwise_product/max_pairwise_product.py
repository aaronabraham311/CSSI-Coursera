# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    
    # First maximum number index:
    max_index_1 = -1

    for i in range(n):
        if (max_index_1 == -1 or (numbers[i] > numbers[max_index_1])):
            max_index_1 = i
    
    # Second maximum number index:
    max_index_2 = -1
    
    for i in range(n):
	    if ((max_index_2 == -1 or (numbers[i] > numbers[max_index_2])) and i != max_index_1):
		    max_index_2 = i
    
    max_product = int(numbers[max_index_1] * numbers[max_index_2])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
