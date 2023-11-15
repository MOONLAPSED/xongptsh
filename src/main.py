import time
from utils.backoff import exponential_backoff

def operation_that_could_fail():
    # This is a placeholder for the operation that could fail.
    # In the real code, this would be replaced with the actual operation.
    pass

def main():
    retries = 0
    while True:
        try:
            operation_that_could_fail()
            break
        except Exception:
            retries += 1
            if retries > 10:
                raise Exception("Operation failed after 10 retries")
            wait_time = exponential_backoff(retries)
            time.sleep(wait_time)

def test_main(mocker):
    mocker.patch('main.operation_that_could_fail', side_effect=Exception)
    with pytest.raises(Exception, match="Operation failed after 10 retries"):
        main()
