import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_average(total, count):
    if count == 0:
        return float('nan') # Return Not a Number for undefined average
    return total / count

try:
    print("Starting calculation...")
    result = calculate_average(100, 0)
    print(f"The average is: {result}")
except Exception as e:
    logging.error("A crash occurred in main.py", exc_info=True)
    print("Program crashed! Check error.log for details.")