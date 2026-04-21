# Today I Did

CLI tool to track work time. 

## Structure 
CLI is structured as a package with "one-file-per-command" structure

```
src/
|--- tid/
|---|--__init__.py
    |-- main.py
    |-- models.py: stores all of the models
    |-- project.py: creates bew project
    |-- start.py: logic to start time entry 
    |-- storage.py: persistence layer 
```

### Commands 
```
tid start --project "<name>" # Start  new time entry 
tid stop # Stops current entry
tid create --name "First Project" -gh "<github-url>" # Create new project
```

### Data models 
Models:
- Project: contains project information
    - name
    - github (optional) - should contain validation
- TimeEntry:
    - start (Y-m-d H:M) 
    - end (Y-m-d H:M)
    - note / title 


