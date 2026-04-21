import typer 

from tid.models import ProjectModel

app = typer.Typer()

@app.command()
def project(name: str, github_url: str = ""):
    project = ProjectModel(name=name, github_url=github_url)
    print(project.name)

if __name__ == "__main__":
    app()
