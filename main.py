import logging

# This tells Python to write any errors into a file called error.log
logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_average(total, count):
    # The bug is here! If count is 0, this crashes.
    return total / count

try:
    print("Starting calculation...")
    # Intentionally causing a ZeroDivisionError by passing 0
    result = calculate_average(100, 0)
    print(f"The average is: {result}")

except Exception as e:
    # If it crashes, log the exact error to error.log
    logging.error("A crash occurred in main.py", exc_info=True)
    print("Program crashed! Check error.log for details.")
