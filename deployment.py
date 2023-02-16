from prefect.deployments import Deployment
from pipeline import main
from prefect.infrastructure.docker import DockerContainer

docker_block = DockerContainer.load("zoom")

docker_dep = Deployment.build_from_flow(
    flow=main,
    name="docker-flow",
    infrastructure=docker_block,
)

if __name__ == "__main__":
    docker_dep.apply()