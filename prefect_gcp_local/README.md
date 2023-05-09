# PREFECT CLOUD PROJECT
>In this mini project, Prefect is used to orchestrate an Extract, Transform, and Load Pipeline application alongside all its dependencies on a docker container
>
>The goal of this project is to test a prefect pipeline in a prebuilt docker environment containing all your parameters without building your code into your container. 
>
>With `bind mounts`, we control the exact mountpoint on the host. We can use this to persist data, but is often used to provide additional data into containers. When working on an application, `we can use a bind mount to mount our source code into the container to let it see code changes, respond, and let us see the changes right away`. This is good for testing
>
>With `prefects remote storage`, we can create a storage block that allows our container instance pull our code from our remote storage and run the code in our instance.

## Build the Docker Image
In the directory of the cloned repo, open the `Dockerfile` and make the changes you need to make. It is well documented, so just follow through.

Once this is done; you can then build the docker image using
```bash
    docker build -t image_name .
```

## Test your Pipeline Locally with the docker using Bind Mounts
The command below allows you test your appliction code contniously without having to build your docker image every single time.
```bash
   docker run -it -v $(pwd):/opt/prefect/flows --platform linux/amd64 image_name bash -c "prefect cloud login -k api_key; python etl_gcs_bq.py"
```
<br>
Note: I am using the --platform flag because the original docker container was built for linux, and I am running it on a Mac.

## Test your Pipeline Locally with Prefect using docker and github as remote storage
1. Create a remote storage block; you can use S3, Github, Gitlab. I created a Github block and I needed only my PAT. 
2. Create a docker infraustructure block and add the image name and tag.
3. Run a prefect deployment block using the command below:
```bash
    prefect deployment build prefect_gcp_local/etl_gcs_bq.py:etl_gcs_to_bq -n docker-test -ib docker-container/zoom -sb github/github-block -q dev -o prefect-docker-deployment
```
- `prefect_gcp_local/etl_gcs_bq.py:etl_gcs_to_bq.py`: Entry point; directory of the file in the repository and the flow function.
- `-n docker-test`: Name of deployment
- `-ib docker-container/zoom`: Name of docker infraustructure
- `-sb github/github-block`: Name of remote storage 
- `-q dev`: Name of work queue
- `-o prefect-docker-deployment`: Name of deployment file

4. Deploy the yaml file to your prefect workspace using `prefect deployment apply prefect-docker-deployment.yaml`

5. Test your deployment by starting your prefect agent in a machine that is configured with your prefect account and has a docker engine running. `prefect agent start -q dev`

Note: 
- If you start the prefect agent on another machine, it must be configurured to the repository the repository is stored.
- You can make changes to the prefect deployment file and reapply  them using the command in (4). This can be useful if you need to change the entrypoint of your code; you might also need to alter some blocks.