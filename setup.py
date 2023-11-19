from setuptools import setup, find_packages

setup(
    name="voiceanalysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai-whisper",
        "soundfile",
        "simple-diarizer",
        "pydub",
        "matplotlib",
        "seaborn",
        "spleeter",
        "jupyterlab",
        "notebook",
        "pytube",
        "moviepy",
        "ffmpeg",
        "ffmpeg-python", 
        "httpx[http2]"
    ],
    dependency_links=[
        "git+https://github.com/artificialnouveau/my-voice-analysis/#egg=my-voice-analysis"
    ],
)
