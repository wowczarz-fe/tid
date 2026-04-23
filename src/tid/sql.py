from contextlib import contextmanager 
from sqlmodel import  Session, SQLModel, create_engine, select
from sqlalchemy.exc import IntegrityError
from tid.models import Project, ProjectBase

class ProjectAlreadyExists(Exception):
    pass

class DB:

    def __init__(self):
        self.path = "database.db"
        self.engine = create_engine(f"sqlite:///{self.path}", echo=True)
        SQLModel.metadata.create_all(self.engine) # Init schema

    @contextmanager
    def session(self):
        s = Session(self.engine)
        try:
            yield s
            s.commit()
        except Exception:
            s.rollback()
            raise
        finally:
            s.close()

def get_projects(session: Session) -> list[Project]:
    return list(session.exec(select(Project)))

def get_project(session, project: ProjectBase) -> list[Project]:
    filters = project.model_dump(exclude_unset=True)
    statement = select(Project).filter_by(**filters)
    return session.exec(statement).all()

def add_project(session: Session, project: ProjectBase) -> None:
    """
    Create new project, commit then populate Project.id
    """
    p = Project.model_validate(project)
    session.add(p)
    try:
        session.flush() # Adds Project.id
    except IntegrityError as e:
        raise ProjectAlreadyExists(project.name) from e

if __name__ == "__main__":
    db = DB()
    p_new = ProjectBase(name="Tes2t", github_url= "http://test.ai")
    with db.session() as s:
        add_project(s, p_new)
        for p in get_projects(s):    
            print(p)
        # print(get_project(s, p_new))
    # engine = create_db()
    # p1 = ProjectBase(name="test", github_url="https://www.test.ai")
    #
    # with Session(engine) as session:
    #     # add_project(p1, session)
    #     s = select(Project)
    #     r = session.exec(s)
    #     for p in r:
    #         print(p)
