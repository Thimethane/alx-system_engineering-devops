Webstack Debugging Project


Overview

This project is part of a series focused on teaching debugging skills related to webstacks. The objective is to troubleshoot and fix issues within a Docker container running Apache web server so that it returns a page containing "Hello Holberton" when queried at the root.

Task

The initial state of the Docker container doesn't return the expected page. After connecting to the container and identifying the issue, the task is to fix the configuration to achieve the desired outcome.

Steps to Fix the Issue

Update the package list and install Apache web server:

bash
Copy code
apt-get update
apt-get install -y apache2
Start the Apache service:

bash
Copy code
service apache2 start
Create an HTML file with the content "Hello Holberton":

bash
Copy code
echo '<html><body>Hello Holberton</body></html>' > /var/www/html/index.html
Access the webpage by querying port 8080 on the Docker container.

Usage
Clone the repository:

bash
Copy code
git clone https://github.com/Thimethane/alx-system_engineering-devops/0x0D-web_stack_debugging_0.git
Navigate to the project directory:

bash
Copy code
cd webstack-debugging
Run the provided fix script inside the Docker container:

bash
Copy code
bash fix_webstack.sh
Access the webpage by querying port 8080 on the Docker container.

Docker Run Example
Run the Docker container with port mapping:

bash
Copy code
docker run -p 8080:80 -d -it holbertonschool/265-0
Expected Result
After following the steps and running the provided fix script, querying port 8080 should return a page containing "Hello Holberton."
