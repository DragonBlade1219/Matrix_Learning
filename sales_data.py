from collections import defaultdict

def sales_data_func(sales_data, frequency_threshold) -> int:
    
    # Diccionario para almacenar la frecuencia de cada cantidad de ventas
    frequency_map = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(sales_data)):
        # Incrementar la frecuencia del elemento actual
        frequency_map[sales_data[right]] += 1
        
        # Verificar si alguna frecuencia excede el umbral
        while max(frequency_map.values()) > frequency_threshold:
            # Reducir la frecuencia del elemento en la posición 'left'
            frequency_map[sales_data[left]] -= 1
            if frequency_map[sales_data[left]] == 0:
                del frequency_map[sales_data[left]]
            left += 1
        
        # Calcular la longitud del subarray actual
        max_length = max(max_length, right - left + 1)
    
    return max_length

def sales_data_func_2(sales_data, frequency_threshold) -> int:
    
    sub_arrays = [];
    current_array = [];
    
    for i in range(len(sales_data)):
        for j in range(i, len(sales_data)):           
            # Incrementar la frecuencia del elemento actual
            current_array.append(sales_data[j]);
            if current_array.count(sales_data[j]) > frequency_threshold:
                current_array.pop();
                sub_arrays.append(current_array.copy());
                current_array.clear();
                break;
            elif j == len(sales_data) - 1:
                sub_arrays.append(current_array.copy());
                current_array.clear();
                break;        
    
    return max(len(sub_array) for sub_array in sub_arrays)


# 1,2,3,4,5,6,7,8,9,1,10,11,12,13