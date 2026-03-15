# pymanager

A lightweight file manager written in Python (work in progress).

Currently pymanager lets you browse folders and files on your computer and open/read simple text files (e.g. .txt, .py). The current path is shown in the top center. Basic navigation (back) and exit are available. Additional features planned: editable path, write mode, support for more file types, improved UI/UX and new design. Doesn't work on Linux!

Badges

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

Features

- Browse folders and view files on the local filesystem.
- Display of current path in the top center.
- Open and read plain text files (.txt, .py, etc.).
- Navigation: Back and Exit buttons.
- Editable path input.
- File write/edit mode.
- Improved UI and design updates.

Planned

- Support for more file formats and previews.
- Support for Linux
- Scrollable text and file Space
- File Info (Metadata usw.)


Screenshots

(Include screenshots or GIFs of the application here when available.)

Currently no screenshots are provided. Add screenshots in the repo's /assets or /docs folder and reference them here.

Installation

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/pymanager.git
cd pymanager
```

2. (Recommended) Install dependencies:

All packages used are integrated in python.

Run Locally

Start the application (replace with the actual entry point file if different):

```bash
python main.py
```


Usage / Examples

- Browse folders using the GUI.
- Click a file (e.g., example.py or notes.txt) to open and read or edit its contents in the viewer.

Notes:
- The whole programm doesn't render correct on Linux
- To test opening files, place a sample .txt or .py file in a folder and navigate to it in pymanager.

Known Issues / Current Bugs

- Can't scroll
- Doesn't work on Linux


Please open an issue with steps to reproduce, platform (OS), and Python version.

Contributing

Contributions are welcome! Suggested workflow:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`.
3. Make changes and add tests where appropriate.
4. Commit and push: `git push origin feature/my-feature`.
5. Open a Pull Request describing your changes.

Please add a CONTRIBUTING.md file with repo-specific guidelines.

License

MIT License

Authors

- Project author: Shadow


Roadmap

Short-term:
- Fix scrolling issue.
- Add more file infos.

Long-term:
- Polished UI/UX and new design.
- Packaging and installer for multiple platforms.
- Add Linux support.

Support

If you encounter issues or want to request features, please open an issue in the repository and include:
- Steps to reproduce
- OS and Python version
- Screenshots or logs (if available)

