import subprocess

class RateLimitExceededError(Exception):
    pass

def run_setup():
    result = subprocess.run(['./setup.sh'], capture_output=True, text=True)
    if 'Error: Setup job has been run too many times. Please wait and try again.' in result.stderr:
        raise RateLimitExceededError('Rate limit exceeded for setup job')
    return result.stdout

def test_run_setup():
    # Test when BASH script runs successfully
    assert run_setup() == 'Running setup job...'
    
    # Test when BASH script fails but not due to rate limiting
    with pytest.raises(subprocess.CalledProcessError):
        run_setup()
    
    # Test when BASH script fails due to rate limiting
    with pytest.raises(RateLimitExceededError):
        run_setup()
