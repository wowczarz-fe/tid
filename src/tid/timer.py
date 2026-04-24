from time import monotonic, sleep
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner


def format_elapsed(seconds: int) -> str:
    """
    Format elapsed seconds
    """    
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def render_text(project: str, task:str, start: int) -> str:
    elapsed = int(monotonic() - start)
    timer = format_elapsed(elapsed)
    return f"[bold blue]{project}[/] [dim]|[/] {task} [blue]{timer}[/]"

def launch_timer(project, task):
    console = Console()
    start = monotonic()
    spinner = Spinner("dots", style="blue")
    with Live(spinner, console=console, refresh_per_second=12) as live:
        while True:
            sleep(0.1)
            spinner.update(text=render_text(project, task, start))
            live.refresh()

if __name__ == "__main__":
    project = "My Project"
    task = "Design timer"
    launch_timer(project, task)    #
