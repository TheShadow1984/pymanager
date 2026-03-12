# pymanager

A lightweight file manager written in Python (work in progress).

Currently pymanager lets you browse folders and files on your computer and open/read simple text files (e.g. .txt, .py). The current path is shown in the top center. Basic navigation (back) and exit are available. Additional features planned: editable path, write mode, support for more file types, improved UI/UX and new design.

Badges

(Place build/test/coverage/license badges here) e.g.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

Features

- Browse folders and view files on the local filesystem.
- Display of current path in the top center.
- Open and read plain text files (.txt, .py, etc.).
- Navigation: Back and Exit buttons.

Planned

- Editable path input.
- File write/edit mode.
- Support for more file formats and previews.
- Improved UI and design updates.

Screenshots

(Include screenshots or GIFs of the application here when available.)

Currently no screenshots are provided. Add screenshots in the repo's /assets or /docs folder and reference them here.

Installation

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/pymanager.git
cd pymanager
```

2. (Recommended) Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

If there is no requirements.txt, install the packages used by the project (add requirements.txt to the repo).

Run Locally

Start the application (replace with the actual entry point file if different):

```bash
python main.py
```

If the project uses a module/GUI entrypoint, update the command accordingly (e.g., `python -m pymanager` or run the appropriate script).

Usage / Examples

- Browse folders using the GUI.
- Click a file (e.g., example.py or notes.txt) to open and read its contents in the viewer.

Notes:
- The path display is read-only for now.
- To test opening files, place a sample .txt or .py file in a folder and navigate to it in pymanager.

Known Issues / Current Bugs

- Can't scroll

(Original note preserved: "Can't scroll")

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

No license file is included in the original README. Add a LICENSE file to make the project's license explicit. A common choice is the MIT License. Example badge above can be updated once a license is added.

Authors

- Project author: (add your name and contact information here)

Add a CONTRIBUTORS or AUTHORS file if there are multiple contributors.

Roadmap

Short-term:
- Fix scrolling issue.
- Add editable path input and write mode.
- Add more file previews.

Long-term:
- Polished UI/UX and new design.
- Packaging and installer for multiple platforms.

Support

If you encounter issues or want to request features, please open an issue in the repository and include:
- Steps to reproduce
- OS and Python version
- Screenshots or logs (if available)

Appendix

Original README content preserved below for reference:

# pymanager
Filemanager written in Python (Still being processed).
At the current state of the Software you can see any Folder and File on your Computer. The current path is shown in the top center but you can't edit it for now. This feature will be added. Also, you have a exit and a back button and you can open and read files like txt py or similar. More files and a write mode will be added soon. New design is also being processed.

Current Bugs:
- Can't scroll