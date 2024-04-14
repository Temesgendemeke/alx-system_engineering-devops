##Postmortem: School Project Website Outage (Due to Nginx Misconfiguration)

### Issue Summary

My personal school project website experienced an outage on Friday, April 5th, 2024, from 10:15 PM PST to 11:00 PM PST. This outage was caused by a misconfiguration in the Nginx web server software. The website was completely inaccessible during this time.

### Timeline

* **10:15 PM PST:**  I noticed my website was unavailable when attempting to access it myself. 
* **10:20 PM PST:**  Checked various online website monitoring tools and confirmed the website was unreachable.
* **10:25 PM PST:**  Reviewed server logs for any error messages. Nginx error logs indicated a configuration error but did not provide specifics.
* **10:50 PM PST:**  Spent time researching common Nginx configuration errors based on the limited information from the logs. 
* **10:45 PM PST:**  Identified a potential issue with the server block configuration for my website. The root directory path might have been incorrectly specified.
* **11:00 PM PST:**  Verified the root directory path in the Nginx configuration file and found a typo. The correct path was updated and the Nginx service was restarted.
* **11:10 PM PST:**  Confirmed the website was functioning normally again.

### Root Cause and Resolution

The root cause of the outage was a typographical error in the Nginx server block configuration file. The path to the website's root directory was incorrectly specified, preventing Nginx from serving the website files. 

The resolution involved identifying the typo in the configuration file, correcting the path to the website's root directory, and restarting the Nginx service. This allowed Nginx to locate and serve the website files correctly.

### Corrective and Preventative Measures

* **Double-check configuration files:**  Before restarting any service, especially critical ones like a web server, double-check the configuration files for typos or errors.
* **Utilize code linters or static analysis tools:**  These tools can help identify potential syntax errors or configuration issues before deployment. 
* **Implement a basic website monitoring tool:**  Even a simple monitoring tool can alert you if your website becomes unavailable, saving you valuable troubleshooting time.
* **Learn from the mistake:**  Document the issue and its resolution for future reference. This will help avoid similar mistakes in future projects.


This experience demonstrates the importance of careful configuration management and the potential impact of seemingly minor errors. By employing these corrective and preventative measures, I can minimize the risk of future outages and ensure the smooth operation of my website projects.  
