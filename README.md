# PREFECT CLOUD X GOOGLE CLOUD
>In this project, Prefect is used to orchestrate an Extract, Transform, and Load Pipeline application alongside all its dependencies on a Google Cloud Environment.
>
>The project focuses on orchestrating the pipeline for the scraper application built in [Project one](https://github.com/paulonye/Smart_Sheet) on Google Compute Engine using Prefect, a more robust framework compared to what was initially done.
>
>The Project is the 6th series in my "Building your first Google Cloud Analytics Project"
>
>[Link to the Yahoo Finance Website](https://finance.yahoo.com/crypto/?.tsrc=fin-srch&offset=0&count=15)
>
>[Link to the Medium Article](https://medium.com/@nwosupaul141/orchestrating-data-pipelines-with-prefect-on-gcp-infrastructure-cdc7aaf42250) 
>
>[Link to the Previous Medium Article](https://medium.com/@nwosupaul141/batching-web-data-into-a-postgres-database-hosted-on-google-cloud-15af1674cdb3)
>
>[Setting your Environment on a Virtual Machine](https://medium.com/@nwosupaul141/optimizing-googles-cloud-infrastructure-for-data-engineering-and-analytics-49d1d91fe7b6)
>
>[Understanding how thw Scraper Application was built](https://medium.com/@nwosupaul141/building-an-etl-pipeline-using-google-service-accounts-85e2a6cfd94d)

## Project Structure

- Setting up the Environment
- Test that the Application works
- Building the Docker Image
- Deploying the Flow
- Running the Deployment

![Cover_Image](https://nwosupaulonye.s3.amazonaws.com/cover5.png)
 
## Set up your environment
Clone the Github Repo 
```bash
   git clone https://github.com/paulonye/prefect_gcp.git
```
Set up your Virtual Environment
```bash
   python -m venv env

   source env/bin/activate
```
Install the Required Libraries in the Virtual Environment
```bash
   pip install -r requirements.txt
```
Authenticate into your Prefect Cloud Workspace on the terminal
```bash
   prefect cloud login

   #Add your API key
```
Confirm that you have the right Google Cloud Credentials set
```bash
   gcloud config list

   gcloud auth application-default login
   #this will allow third party application access
```
## Test that the Application works
Enure you have created all the necesary blocks in your prefect cloud workspace
`python pipeline.py`

## Build the Docker Image
In the directory of the cloned repo, open the `Dockerfile` and make the changes you need to make. It is well documented, so just follow through.

Once this is done; you can then build the docker image using
```bash
    docker build -t image_name .
```
The above command builds the docker image; to test that it works, use:
```bash
   docker run image_name

   #this should return nothing because we did not set an entrypoint
```
 ## Deploying the Flow
 To deploy the flow, ensure you create the docker block on your prefect cloud workspace.
 Run the command to deploy
```bash
   python deployment.py
```
Once the deployment has been made, navigate to the workspace to add the necessary parameters.

## Running the Deployment
To run the deployment, we need to set the prefect agent in our environment
For this, we need to set it up a detached environment, and we can do this using `tmux`
```bash
    tmux
    #this opens a new terminal window

    source emv/bin/activate
    #activate the virtual environment where you installed prefect

    prefect agent start -q "default"
    #deploy the prefect agent to pickup workqueues using the default tag

    ctrl+D, B
    #detach from the tmux window

    tmux ls
    #list the tmux sessions currently running

    tmux attach -t 0
    #reattach to the tmux session

    tmux kill-session -t 0
    #kill the session
```
You can then schedule the deployment on your prefect cloud workspace