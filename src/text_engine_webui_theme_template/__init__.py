"""Template theme for text-game-webui."""
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent


class TemplateTheme:
    """Entry-point theme class discovered by text-game-webui."""

    name = "My Custom Theme"
    description = "A starter template theme — edit tokens.yaml and rebuild."
    author = "Your Name"
    css_path = str(_PKG_DIR / "theme.css")
    __file__ = str(_PKG_DIR / "__init__.py")
