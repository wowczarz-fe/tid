from pydantic import BaseModel, HttpUrl,  Field

class ProjectModel(BaseModel):
    name: str = Field(min_length=1)
    github_url: str = HttpUrl

