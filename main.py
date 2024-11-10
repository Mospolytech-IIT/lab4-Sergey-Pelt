"""Main"""
from functions import division_ex, index_ex, safe_file_read, safe_division
from functions import different_ex, different_ex_2, different_ex_3, generate_ex, check_value

if __name__ == "__main__":
    try:
        print(division_ex(10, 1))
        print(index_ex([1, 2, 3], 1))
        print(safe_file_read("example.txt"))
        print(safe_division(10, 0))
        print(different_ex(-1))
        print(different_ex_2("Hello"))
        print(different_ex_3([10, 0, 5]))
        print(generate_ex(-5))
        print(check_value(150))
    except Exception as e:
        print(f"Необработанное исключение: {e}")
