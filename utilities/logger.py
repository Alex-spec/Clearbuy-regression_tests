import datetime
import os

class Logger:
    logs_dir = r"C:\Users\PC\PycharmProjects\pythonProject\Clearbuy-regression_tests\logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    file_name = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def info(cls, message: str):
        time_stamp = str(datetime.datetime.now())
        log_line = f"{time_stamp} - INFO - {message}\n"
        cls.write_log_to_file(log_line)

    @classmethod
    def error(cls, message: str):
        time_stamp = str(datetime.datetime.now())
        log_line = f"{time_stamp} - ERROR - {message}\n"
        cls.write_log_to_file(log_line)

    @classmethod
    def debug(cls, message: str):
        time_stamp = str(datetime.datetime.now())
        log_line = f"{time_stamp} - DEBUG - {message}\n"
        cls.write_log_to_file(log_line)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'Unknown Test')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n\n-----\n"

        cls.write_log_to_file(data_to_add)
