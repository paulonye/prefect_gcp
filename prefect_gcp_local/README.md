# PREFECT CLOUD PROJECT
>In this mini project, Prefect is used to orchestrate an Extract, Transform, and Load Pipeline application alongside all its dependencies on a docker container
>
>The goal of this project is to show how you can test a prefect pipeline in a prebuilt docker environment containing all your parameters.
>
>With `bind mounts`, we control the exact mountpoint on the host. We can use this to persist data, but is often used to provide additional data into containers. When working on an application, `we can use a bind mount to mount our source code into the container to let it see code changes, respond, and let us see the changes right away`.


## Build the Docker Image
In the directory of the cloned repo, open the `Dockerfile` and make the changes you need to make. It is well documented, so just follow through.

Once this is done; you can then build the docker image using
```bash
    docker build -t image_name .
```

## Test your Pipeline with the docker using Bind Mounts
The command below allows you test your appliction code contniously without having to build your docker image every single time.
```bash
   docker run -it -v $(pwd):/opt/prefect/flows --platform linux/amd64 image_name bash -c "prefect cloud login -k api_key; python etl_gcs_bq.py"
```
<br>
Note: I am using the --platform flag because the original docker container was built for linux, and I am running it on a Mac.
