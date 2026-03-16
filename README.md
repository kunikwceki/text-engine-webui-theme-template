# text-engine-webui-theme-template

A starter template for creating custom themes for
[text-game-webui](https://github.com/bghira/text-game-webui).

## Quick Start

1. Clone this repo and rename the package.
2. Edit `src/text_engine_webui_theme_template/tokens.yaml` with your colors.
3. Run `python build_theme.py` to regenerate `theme.css` and `tokens.json`.
4. Install into your webui environment:

```bash
pip install -e .
```

5. Restart text-game-webui and select your theme in Settings > Appearance.

## Structure

```
src/text_engine_webui_theme_template/
  __init__.py       # Entry-point class
  tokens.yaml       # Design tokens (edit this)
  tokens.json       # Generated
  theme.css         # Generated
  assets/
    images/         # Optional theme images
    sounds/         # Optional theme sounds
```

## How It Works

The `setup.py` declares an entry point under `text_game_webui.themes`.
When text-game-webui starts, it discovers all installed packages that
provide this entry point and makes them available in the theme dropdown.

## Local Development (Without pip install)

You can also place your theme folder directly in
`~/.text-game-webui/themes/my-theme/` with a `theme.json` and `theme.css`
file. This method does not require a pip package.
