# Load Balancer Project

This project automates the setup of a load balancer and web servers using HAProxy and Nginx.

## Setup Instructions

### Web Servers (web-01 and web-02)

1. Run the `0-custom_http_response_header` script on both web servers to configure Nginx and add a custom HTTP response header.

```bash
./0-custom_http_response_header
Replace [STUDENT_ID] with your actual student ID in the Nginx configuration.

Load Balancer (lb-01)

Run the `1-install_load_balancer`` script on the load balancer to install and configure HAProxy.
./1-install_load_balancer
Replace [STUDENT_ID] with your actual student ID in the HAProxy configuration.

Custom HTTP Response Header

The Nginx configuration adds a custom HTTP response header X-Served-By to identify the serving web server.

Usage
After setting up the web servers and load balancer, the system will distribute requests to web servers using a round-robin algorithm.

You can test by sending HTTP requests to the load balancer IP and observing the X-Served-By header in the response.
curl -Is [LOAD_BALANCER_IP]

Contributer: Timothee RINGUYENEZA <thimethane@gmail.com>
