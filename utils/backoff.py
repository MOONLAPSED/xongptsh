def exponential_backoff(retries: int) -> float:
    return min(2 ** retries, 60)


def test_exponential_backoff():
    assert exponential_backoff(0) == 1
    assert exponential_backoff(1) == 2
    assert exponential_backoff(4) == 16
    assert exponential_backoff(6) == 60
    assert exponential_backoff(10) == 60
