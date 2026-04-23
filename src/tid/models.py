from pydantic import BaseModel, HttpUrl,  Field, field_validator
from sqlmodel import Field, SQLModel

class ProjectBase(SQLModel):
    name: str = Field(min_length=1, unique=True)
    github_url:  str

    # @field_validator("github_url")
    # def validate_gh(cls, v:str) -> str:
    #     HttpUrl(v) # Raise ValueError if not url - SQLAlchemy has no URL type
    #     return v

class Project(ProjectBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
