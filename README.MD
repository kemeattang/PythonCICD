## Security Policies and Tools

## Overview
This documentation provides details on the security policies enforced in the CI/CD pipeline and the tools used to ensure application and infrastructure security.

## Security Policies
1. Dependency Management
Policy: Ensure all application dependencies are scanned for vulnerabilities.
Implementation:
Use Snyk to scan for vulnerabilities in third-party libraries and dependencies.
Automatically fail builds if critical vulnerabilities are detected.
2. Container Security
Policy: All container images must be scanned for vulnerabilities before deployment.
Implementation:
Use Trivy to perform static scans of container images.
Flag and fail builds if high-severity vulnerabilities are identified in base images or application layers.
3. Dynamic Application Security Testing (DAST)
Policy: Ensure the running application is tested for runtime vulnerabilities and security misconfigurations.
Implementation:
Use OWASP ZAP for active security scans against live applications.
Generate reports highlighting vulnerabilities like SQL Injection, XSS, and more.