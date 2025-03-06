# :red_square: Vuln Scan v1.0 - _The Multi-Tool Web Vulnerability Scanner_
_**VulnScan has been ported to Python3 i.e. v1.0**. The Python2.7 codebase is available on v1.1 releases section. Download and use it if you still haven't upgraded to Python 3. Kindly note that the v1.1 (Python2.7) will not be enhanced further._


## Evolution:
> It is quite a fuss for a pentester to perform _**binge-tool-scanning**_ (_running security scanning tools one after the other_) sans automation. Unless you are a pro at automating stuff, it is a herculean task to perform binge-scan for each and every engagement. The ultimate goal of this program is to solve this problem through automation; viz. **running multiple scanning tools to discover vulnerabilities, effectively judge false-positives, collectively correlate results** and **saves precious time**; all these under one roof.<p>Enter **python vulnscan.py websitename**.


## Features
Here’s a refined version of your feature statements while keeping them clear and impactful:  

- **Effortless installation** with a single-step setup.  
- **Integrates multiple security scanning tools** alongside custom-coded checks, providing instant results.  
- **Runs a suite of powerful tools**, including `nmap, dnsrecon, wafw00f, uniscan, sslyze, fierce, lbd, theharvester, amass, and nikto`, all within a unified framework.  
- **Significantly reduces scanning time**, optimizing efficiency.  
- **Cross-verifies vulnerabilities** using multiple tools, minimizing false positives for accurate results.  
- **Lightweight and resource-efficient**, ensuring minimal system impact.  
- **Highlights time-intensive tests** with legends, allowing users to skip lengthy scans using `Ctrl+C`.  
- **Aligns with OWASP Top 10 & CWE 25** to ensure comprehensive vulnerability detection. *(In progress)*  
- **Categorizes findings by severity levels**—critical, high, medium, low, and informational.  
- **Provides vulnerability insights**, explaining security risks and their potential impact.  
- **Offers remediation guidance**, detailing steps to mitigate identified vulnerabilities.  
- **Generates an executive summary**, delivering a concise overview of discovered vulnerabilities by severity.  
- **Leverages AI-driven automation** to trigger additional scans based on detected vulnerabilities, such as automatically launching `wpscan` and `plecost` when a WordPress site is identified. *(In progress)*  
- **Generates in-depth reports in PDF format**, documenting scan results and tool usage for future reference. *(In progress)*  
- **Executes Metasploit auxiliary modules on demand**, enhancing vulnerability discovery. *(In progress)*  


## Vulnerability Checks
- :heavy_check_mark: DNS/HTTP Load Balancers & Web Application Firewalls.
- :heavy_check_mark: Checks for Joomla, WordPress and Drupal
- :heavy_check_mark: SSL related Vulnerabilities (_HEARTBLEED, FREAK, POODLE, CCS Injection, LOGJAM, OCSP Stapling_).
- :heavy_check_mark: Commonly Opened Ports.
- :heavy_check_mark: DNS Zone Transfers using multiple tools (_Fierce, DNSWalk, DNSRecon, DNSEnum_).
- :heavy_check_mark: Sub-Domains Brute Forcing (_DNSMap, amass, nikto_)
- :heavy_check_mark: Open Directory/File Brute Forcing.
- :heavy_check_mark: Shallow XSS, SQLi and BSQLi Banners.
- :heavy_check_mark: Slow-Loris DoS Attack, LFI (_Local File Inclusion_), RFI (_Remote File Inclusion_) & RCE (_Remote Code Execution_).
- & more coming up...

## Requirements
- **Python 3**
- Kali OS (_**Preferred**, as it is shipped with almost all the tools_)
- Tested with Parrot & Ubuntu Operating Systems.

## Usage 
 `python3 vulnscan.py example.com`

https://user-images.githubusercontent.com/6489729/138737524-9c4dc567-ec78-40b4-9a7b-8ff52d5dc98b.mp4


## Installation

Alternatively, your can install the `vulnscan` python module with `pip`. This will create a link for `vulnscan` in your PATH. 

```
Create a directory at any location you want.
git clone https://github.com/Gowtham0896/VulnScan.git
python3 -m pip install .
python vulnscan.py example.com
```

