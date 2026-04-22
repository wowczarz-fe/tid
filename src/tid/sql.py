from sqlmodel import  Session, SQLModel, create_engine, select

from tid.models import Project, ProjectBase

def create_db():
    db = "database.db"
    engine = create_engine(f"sqlite:///{db}", echo=True)
    SQLModel.metadata.create_all(engine)
    return engine

def add_project(in_project: ProjectBase, session: Session) -> Project:
    # Insert new project based on CLI input
    p = Project.model_validate(in_project) # Validate 
    session.add(p)
    session.commit()
    session.refresh(p) # Populate Project.id 
    return p

if __name__ == "__main__":

    engine = create_db()
    p1 = ProjectBase(name="test", github_url="https://www.test.ai")

    with Session(engine) as session:
        add_project(p1, session)
        s = select(Project)
        r = session.exec(s)
        for p in r:
            print(p)
