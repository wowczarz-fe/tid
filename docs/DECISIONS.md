# DESIGN DECISIONS

1. Keep it minimal as POC to practice coding rather than full well scoped project.

## Storage 
Main storage layer will be SQLLite DB it will consists of two tables:
- Projects: store project metadata:
    - id (key)
    - name (str)
    - github (url)
- Entries: all entries table with:
    - id
    - project_id (join key with project table)
    - start (datetime) 
    - end (datetime)

## Use typer as CLI interface 
    https://typer.tiangolo.com/


