from matrix_addition import matrix_addition
from matrix_multiplication import matrix_multiplication
from rotate_matrix_90_degrees import rotate_matrix_90_degrees
from sales_data import sales_data_func, sales_data_func_2
from shifted_vowels import shifted_vowels
from time_travel import time_travel
from transpose_matrix import transpose_matrix

def main():

    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];

    matrix_2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ];    

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ];

    matrix2 = [
        [7, 8],
        [9, 10],
        [11, 12]
    ];
        
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];     

    matrix_b = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];
    
    result_1 = matrix_addition(matrix_1, matrix_2);
    print("Resultant Matrix:");
    for row in result_1:
        print(row);
    
    result_2 = matrix_multiplication(matrix1, matrix2);
    print("Resultant Matrix:");
    for row in result_2:
        print(row);
    
    transpose = transpose_matrix(matrix_a);
    print("Transposed Matrix:");
    for row in transpose:
        print(row);

    rotated = rotate_matrix_90_degrees(matrix_b);
    print("Rotated Matrix:");
    for row in rotated:
        print(row);
    
#########################################################################################
 
# PRUEBA CAPITAL ONE   

    """
    Ejercicio 1: 
    Imagine that you have a time machine. You are 
    given an array "years". You start in the 
    year[0]. First, you want t travel to year[1], 
    then year[2], and so on. Your task is to calculate 
    the time required to visit all the years from the 
    list in order.
    
    The time required to travel from the year A to the 
    year B  is calculated as follows:
    - 0 hours if A = B
    - 1 hour if A < B
    - 2 hours if A > B
    
    """
    years = [
                [1990, 2000, 1998, 2015, 2014],   # 6 años en viaje (MIX)
                [2024, 2023, 2022, 2021, 2020],   # 8 años en viaje (BACKWARD)
                [1990, 1991, 1998, 1999, 2000],   # 4 años en viaje (FORKWARD)
                [1990, 2000, 2011, 2012, 1990],   # 5 años en viaje (MIX)
            ];
    
    print(time_travel(years[0]));
    print(time_travel(years[1]));
    print(time_travel(years[2]));
    print(time_travel(years[3]));
    
    #########################################################################################
    """
    Ejercicio 2:
    
    Given a String "message", your task is to swift each vowel 
    to the position of the next vowel in the string. The last 
    vowel should be shifted to the position of first  vowel 
    of the string. See the example for the detailed 
    explanation:
    
    Example: 
        input: codesignal
        output: cadosegnil
        
    The list of vowels are: "a", "e", "i", "o", "u"
    
    """
    
    print(shifted_vowels("codesignal"));
    print(shifted_vowels("aeiou"));
    print(shifted_vowels("murcielago"));
    print(shifted_vowels("code signal"));
    print(shifted_vowels("kkk"));
    
        #########################################################################################
    """
    Ejercicio 3:
    
    In a retail store, you are in chargeof analyzing patterns in product 
    sales to optimaze inventory. You have an array of positive integers, 
    "sales_data", where each integer represents the sales amount on a 
    given day. Additionally, you have a positive integer 
    "frecuency_threshold" wich specifies the maximum 
    allowed frecuency of any sales amount within a 
    contiguos subarray.
    
    """
    
    frequency_threshold = 2
    sales_data_1 = [1, 2, 2, 3, 1, 4, 2, 2]; # 6
    sales_data_2 = [1, 1, 2, 1, 3, 4, 5, 6, 1]; # 7
    sales_data_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 10, 11, 12 ,13]; # 12
    
    print(sales_data_func_2(sales_data_1, frequency_threshold));
    print(sales_data_func_2(sales_data_2, frequency_threshold));
    print(sales_data_func_2(sales_data_3, frequency_threshold));
    
if __name__ == "__main__":
     main();