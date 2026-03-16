from setuptools import setup, find_packages

setup(
    name="text-engine-webui-theme-template",
    version="0.1.0",
    description="Template theme for text-game-webui",
    author="Your Name",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "text_engine_webui_theme_template": [
            "theme.css",
            "tokens.yaml",
            "tokens.json",
            "assets/images/*",
            "assets/sounds/*",
        ],
    },
    entry_points={
        "text_game_webui.themes": [
            "my-custom-theme=text_engine_webui_theme_template:TemplateTheme",
        ],
    },
    python_requires=">=3.10",
)
