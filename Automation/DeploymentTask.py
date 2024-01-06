# Automation Script: Create a script that automates a repetitive task, such as deploying a new version of a web application or setting up a development environment.

import subprocess

def deploy_web_application(version):
    # Step 1: Pull the latest code from the repository
    print("Step 1: Pulling the latest code from the repository")
    subprocess.run(["git", "pull"])

    # Step 2: Build the web application
    print("Step 2: Building the web application")
    subprocess.run(["npm", "install"])
    subprocess.run(["npm", "run", "build"])

    # Step 3: Stop the existing web server
    print("Step 3: Stopping the existing web server")
    subprocess.run(["sudo", "service", "nginx", "stop"])

    # Step 4: Copy the new build to the web server
    print("Step 4: Copying the new build to the web server")
    subprocess.run(["cp", "-r", "dist/*", "/var/www/html"])

    # Step 5: Start the web server
    print("Step 5: Starting the web server")
    subprocess.run(["sudo", "service", "nginx", "start"])

    # Step 6: Verify the deployment
    print("Step 6: Verifying the deployment")
    response = subprocess.run(["curl", "-s", "http://localhost"], capture_output=True)
    if response.returncode == 0 and b"Welcome to the web application" in response.stdout:
        print("Deployment successful!")
    else:
        print("Deployment failed.")

# Specify the version to deploy
version = "1.2.3"

# Call the deploy_web_application function
deploy_web_application(version)
