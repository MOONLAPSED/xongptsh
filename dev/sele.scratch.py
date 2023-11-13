from selenium import webdriver
import time
import subprocess

# Start a new Chrome browser session
driver = webdriver.Chrome()

# Navigate to the web page with queries and responses
driver.get("https://your-web-page-url")

# Wait for the page to load (adjust wait time as needed)
time.sleep(5)
# Extract queries and responses (modify these selectors based on your page structure)
queries = driver.find_elements_by_css_selector(".query-class")
responses = driver.find_elements_by_css_selector(".response-class")

# Log queries and responses to a text file

log_file_path = "queries_responses_log.txt"
with open(log_file_path, "a") as log_file:
    for query, response in zip(queries, responses):
        log_file.write(f"Query: {query.text}\n")
        log_file.write(f"Response: {response.text}\n")
        log_file.write("\n")

# Close the browser
driver.quit()
