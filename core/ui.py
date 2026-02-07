from rich.console import Console
from rich.panel import Panel

console = Console()

def header(title):
    console.print(Panel.fit(f"[bold cyan]{title}[/bold cyan]", border_style="cyan"))

def menu():
    console.print("""
[1] Phone Intelligence
[2] Username Scanner
[3] Telegram Intelligence
[4] Link Tracker
[5] Inspector
[6] Generate HTML Report
[0] Exit
""")
