- Network Traffic Analysis

Overview

This project involves analyzing network traffic using Wireshark to identify and inspect HTTP and TCP packets. The goal is to capture login credentials sent over HTTP, analyze network requests for potential security risks, and propose mitigation strategies.

Steps Performed
	1.	Identify the Local IP Address:
	•	Used ifconfig to retrieve the local IP.
	•	Stored it in a file named ips.txt.
	2.	Search for Targets:
	•	Opened Firefox and searched for:
	•	testphp.vuln
	•	Port Swigger
	3.	Ping Targets to Retrieve IPs:
	•	Used ping to get the IP addresses of both domains.
	•	Appended these IPs to ips.txt.
	4.	Monitor Traffic Using Wireshark:
	•	Opened Wireshark and filtered packets using tcp.
	•	Checked all collected IPs to find any unknown or suspicious ones.
	•	Investigated the unknown IP using VirusTotal (no threats detected).
	5.	Intercept Login Credentials:
	•	Opened the login page of testphp.vuln.
	•	Entered credentials: user: test, pass: test.
	•	Switched to Wireshark and filtered packets using http.
	•	Located the transmitted username and password in plain text.

Analysis of Potential Security Threats

1. Credentials Exposure Over HTTP
	•	The captured credentials (test:test) were transmitted in plaintext, making them vulnerable to Man-in-the-Middle (MITM) attacks.
	•	Any attacker on the same network could easily intercept and steal login details.

2. Unencrypted Communication
	•	The traffic analysis confirmed that HTTP (port 80) was used instead of HTTPS (port 443).
	•	Lack of encryption means that session tokens, cookies, and sensitive data could be intercepted.

3. Unexpected IP Discovery
	•	During the tcp filtering process, an unrecognized IP was identified.
	•	VirusTotal analysis showed no immediate threats, but monitoring unexpected connections is crucial.

4. Lack of Security Headers
	•	No security headers such as HSTS, Content Security Policy (CSP), or X-Frame-Options were detected.
	•	This increases the risk of attacks like Clickjacking, Cross-Site Scripting (XSS), and Downgrade Attacks.

Recommendations to Mitigate Risks

✅ Enforce HTTPS:
	•	Implement SSL/TLS certificates to encrypt data in transit.
	•	Use HSTS (HTTP Strict Transport Security) to prevent protocol downgrades.

✅ Secure Authentication Mechanisms:
	•	Use hashed & salted passwords instead of transmitting them in plaintext.
	•	Implement multi-factor authentication (MFA) for added security.

✅ Monitor Unusual Traffic Patterns:
	•	Regularly analyze network traffic using Wireshark & Intrusion Detection Systems (IDS).
	•	Log and investigate unexpected outbound connections.

✅ Apply Security Headers:
	•	Implement Content Security Policy (CSP) to prevent XSS attacks.
	•	Use X-Frame-Options: DENY to mitigate Clickjacking risks.

✅ Limit Exposure to Open Networks:
	•	Avoid accessing sensitive services over public Wi-Fi without VPN encryption.

Tools Used
	•	ifconfig (to find local IP)
	•	ping (to retrieve target IPs)
	•	Wireshark (to capture and analyze network packets)
	•	VirusTotal (to check for malicious IPs)

Conclusion

This analysis demonstrates the risks associated with transmitting sensitive information over unencrypted HTTP connections. By implementing encryption, security headers, and network monitoring, organizations can reduce the risk of credential theft and unauthorized access.

