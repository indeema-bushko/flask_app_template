# flask_app_template
Project template with basic structure for the Flask web application

# Add script to manage flask server application as a system service
copy: ./flask_app_template shell script to /etc/init.d folder

# Make script executable.
sudo chmod 755 /etc/init.d/flask_app_template

# Update system daemon control.
sudo systemctl daemon-reload

use 'service flask_app_template start|stop|restart' to manage service life cycle 

# Start up service on system boot run command: 
sudo update-rc.d flask_app_template defaults
