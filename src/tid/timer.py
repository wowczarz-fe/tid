import time 
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.live import Live
from rich.console import Group
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

def main():
    second = 0
    spinner = SpinnerColumn()
    text = TextColumn("...")
    timer = TimeElapsedColumn()
    progress = Progress(spinner, text, timer, transient=True)
    with progress:
        try:
            progress.add_task("")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

def main():
    from rich.panel import Panel

    second = 0
    spinner = SpinnerColumn()
    text = TextColumn("...")
    timer = TimeElapsedColumn()
    progress = Progress(spinner, text, timer, transient=True)
    panel = Panel(progress, title="[bold]tid[/bold] – working", subtitle="Ctrl-C to close", subtitle_align="right")

    with Live(panel, refresh_per_second=1, transient=True):
        progress.add_task("", total=None)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
def main():
    progress = Progress(SpinnerColumn(), TimeElapsedColumn())
    hint = Text("Press Ctrl-C to close watch (timer keeps running)", style="dim italic")
    display = Group(progress, hint)

    with Live(display, refresh_per_second=1, transient=True):
      progress.add_task("", total=None)
      try:
          while True:
              time.sleep(1)
      except KeyboardInterrupt:
          pass
if __name__ == "__main__":
    main()
