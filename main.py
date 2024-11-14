"""Main"""
from functions import all_ex
if __name__ == "__main__":
    try:
        all_ex()
    except Exception as e:
        print(f"Необработанное исключение: {e}")
