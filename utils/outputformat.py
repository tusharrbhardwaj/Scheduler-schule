from rich.console import Console

console = Console()

def success(message):
    console.print(f"[bold green]✔ {message}[/bold green]")

def error(message):
    console.print(f"[bold red]✘ {message}[/bold red]")

def info(message):
    console.print(f"[white]➜ {message}[/white]")

def warning(message):
    console.print(f"[bold yellow]⚠ {message}[/bold yellow]")

def heading(message):
    console.print(f"\n[bold cyan]{message}[/bold cyan]")