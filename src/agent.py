import time
from utils.backoff import exponential_backoff

def operation1_that_could_fail():
    pass

def operation2_that_could_fail():
    pass

def agent_main():
    retries = 0
    while True:
        try:
            operation1_that_could_fail()
            operation2_that_could_fail()
            break
        except Exception:
            retries += 1
            if retries > 10:
                raise Exception("Operation failed after 10 retries")
            wait_time = exponential_backoff(retries)
            time.sleep(wait_time)

def test_agent_main(mocker):
    mocker.patch('agent.operation1_that_could_fail', side_effect=Exception)
    mocker.patch('agent.operation2_that_could_fail', side_effect=Exception)
    with pytest.raises(Exception, match="Operation failed after 10 retries"):
        agent_main()
