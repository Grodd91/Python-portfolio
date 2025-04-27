
# YT-PAO - YouTube Playlist Analyzer & Organizer

YT-PAO is a powerful tool designed to analyze and organize YouTube playlists. Whether you prefer working with a graphical interface or through the command line, YT-PAO allows you to efficiently extract data from playlists, archive them, track removed videos, and export data in various formats.

## Features

- **Playlist Analysis**: Extract and view data from YouTube playlists, including video titles, URLs, durations, uploaders, view counts, and availability status.
- **Multiple Output Formats**: Generate reports in `cmd`, `txt`, `json`, `csv`, `html`, or save to a MySQL database.
- **Work Modes**: Choose from different modes: `all` (all videos), `unavailable` (only unavailable videos), `available` (only available videos).
- **Archiving**: Create local copies of reports in the `Output` folder, organized by playlist name.
- **Graphical User Interface (GUI)**: Organize and view YouTube playlists interactively with a GUI, supporting features like playlist export and video status tracking.
- **Command-Line Interface (CLI)**: Command-line version for generating playlist reports, suitable for automated usage and batch processing.

## Requirements

To run YT-PAO, you need Python 3.x and several external libraries. You can install them using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Python-portfolio/YTPAO.git
   ```
2. Navigate to the project directory:
   ```bash
   cd YTPAO
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Graphical User Interface (GUI) Usage

To use the GUI version of YT-PAO, simply run the application:

```bash
python3 ui.py
```

The GUI will prompt you to enter a YouTube playlist link, select output format, and choose the desired report mode (all, unavailable, or available). It will then display results interactively and allow you to save them.

### Command-Line Interface (CLI) Usage

Basic usage of the program:

```bash
python3 main.py --playlistLink <playlist_link> --resultFormat <output_format> --listMode <work_mode>
```

### Flags

- `--playlistLink`: The link to the YouTube playlist (required).
- `--resultFormat`: The output format. Available options: `cmd`, `txt`, `json`, `csv`, `html`, `mySQL`.
- `--listMode`: The work mode. Available options: `all` (all videos), `unavailable` (only unavailable videos), `available` (only available videos).

### Examples

1. **Display results in the console**:
   ```bash
   python3 main.py --playlistLink https://www.youtube.com/playlist?list=PL1234567890 --resultFormat cmd --listMode all
   ```

2. **Generate a report in JSON format**:
   ```bash
   python3 main.py --playlistLink https://www.youtube.com/playlist?list=PL1234567890 --resultFormat json --listMode unavailable
   ```

3. **Save the report to a MySQL database**:
   ```bash
   python3 main.py --playlistLink https://www.youtube.com/playlist?list=PL1234567890 --resultFormat mySQL --listMode all
   ```

### Available Output Formats

- **cmd**: Prints the report in the console in a formatted text table.
- **txt**: Saves the report as a plain text file.
- **json**: Saves the report as a JSON file.
- **csv**: Saves the report as a CSV file.
- **html**: Generates an HTML report with a web-style layout.
- **mySQL**: Saves the report to a MySQL database.

## File Structure

- `main.py`: Command-line tool for playlist analysis and reporting.
- `ui.py`: GUI-based tool for organizing and viewing playlists.
- `Output/`: Folder where reports are saved. Each playlist has its own subfolder named after the playlist.
- `web_template/`: HTML and CSS templates used for generating HTML reports.
- `config.yaml`: Configuration file containing MySQL database connection details.
- `requirements.txt`: List of required Python libraries.

## Authors

- **Kordight** - [GitHub](https://github.com/Kordight)
- **Grodd91** - [GitHub](https://github.com/Grodd91)
