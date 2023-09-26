Nginx Configuration Automation


This project provides Bash scripts to automate the configuration of an Nginx web server on Ubuntu, meeting specific requirements such as redirection, custom 404 pages, and more.

Scripts


1-install_nginx_web_server

This script installs Nginx on a Ubuntu machine and configures it to listen on port 80. It ensures that querying Nginx at its root ("/") with a GET request returns "Hello World!"

3-redirection

Configures Nginx to redirect the "/redirect_me" route to another specified page using a "301 Moved Permanently" response.

4-not_found_page_404

Configures Nginx to have a custom 404 page that returns an HTTP 404 error code along with the string "Ceci n'est pas une page".

Usage

Make the scripts executable using chmod +x <script_name>.
Run the desired script using ./<script_name>. For example: ./1-install_nginx_web_server.

Example

After running the scripts, Nginx will be configured based on the specified requirements. For example:

Accessing http://<your_ip_address>/redirect_me will result in a 301 redirect to the specified page.
Accessing a non-existent page will return a 404 error with the custom page displaying "Ceci n'est pas une page".

Notes

Ensure you have appropriate permissions to execute the scripts and configure Nginx.
These scripts are designed for Ubuntu machines. Adjustments may be needed for other distributions.
For security reasons, ensure your server is appropriately configured before deploying in a production environment.