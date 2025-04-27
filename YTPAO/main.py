import argparse
import os
import re
import sys
import json
import yaml
from datetime import datetime
from ytdlp_parser import parse_playlist
from html_manager import generate_html_list, read_html_template, extract_head_and_body, generate_html_list_invalid_videos
from mySQL_manager import add_report, create_database

# Function to process YouTube playlist URL and extract the playlist ID.
def process_playlist_URL(playlist_URL):
    pattern = r'(?:list=)([a-zA-Z0-9_-]+)'  # Regular expression to find the playlist ID in the URL
    match = re.search(pattern, playlist_URL)
    if match:
        playlist_id = match.group(1)  # Extract the playlist ID
        return f'https://www.youtube.com/playlist?list={playlist_id}'  # Return the full playlist URL
    
    # If URL is invalid, print an error message and exit.
    print(json.dumps({"success": False, "error": "URL is not a valid YouTube playlist URL!"}))
    sys.exit(1)

# Function to parse command-line arguments.
def parse_args():
    parser = argparse.ArgumentParser(description="Interpretation of flags and YouTube playlist link.")
    # Define arguments for playlist link, result format, and list mode
    parser.add_argument('--playlistLink', type=str, required=True, help="The YouTube playlist link.")
    parser.add_argument('--resultFormat', type=str, required=True, choices=['cmd', 'txt', 'json', 'mySQL', 'csv', 'html'],
                        help="The report format. Available options: cmd, txt, json, mySQL, csv, html.")
    parser.add_argument('--listMode', type=str, required=True, choices=['all', 'unavailable', 'available'],
                        help="The work mode. Available options: all, unavailable, available.")
    return parser.parse_args()

# Function to format the table into a human-readable string.
def format_table(headers, rows):
    # Calculate the maximum width for each column based on the content.
    column_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]
    # Create the header row with proper alignment.
    header_row = " | ".join(f"{header:{width}}" for header, width in zip(headers, column_widths))
    # Create the separator row.
    separator = "-+-".join("-" * width for width in column_widths)
    # Create the data rows.
    data_rows = "\n".join(
        " | ".join(f"{str(cell):{width}}" for cell, width in zip(row, column_widths)) for row in rows
    )
    return f"{header_row}\n{separator}\n{data_rows}"

# Function to compose the text tables for playlist and video data.
def compose_text_table(playlist_data, videos):
    playlist_headers = ["Key", "Value"]
    playlist_rows = list(playlist_data.items())
    playlist_table = format_table(playlist_headers, playlist_rows)

    # Define headers for the video data table.
    video_headers = ["Lp", "Title", "URL", "Duration", "Uploader", "Uploader URL", "Approximate View Count", "bValid"]
    video_rows = []

    # Populate the video data rows.
    for index, video in enumerate(videos):
        video_row = [
            index + 1,
            getattr(video, 'title', 'N/A'),
            getattr(video, 'url', 'N/A'),
            getattr(video, 'duration', 'N/A'),
            getattr(video, 'uploader', 'N/A'),
            getattr(video, 'uploader_url', 'N/A'),
            getattr(video, 'view_count', 'N/A'),
            getattr(video, 'valid', 'N/A')
        ]
        video_rows.append(video_row)

    video_table = format_table(video_headers, video_rows)
    return playlist_table, video_table

# Function to load database configuration from the config file.
def load_db_config():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config['database']

# Main function to drive the program.
def main():
    # Parse command-line arguments.
    args = parse_args()
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Get the current date and time for filenames.

    try:
        # Attempt to parse the playlist and get video data.
        playlist_data, videos = parse_playlist(process_playlist_URL(args.playlistLink), args.listMode)
    except Exception as e:
        # Handle any errors during playlist parsing.
        print(json.dumps({"success": False, "error": f"Error parsing playlist: {str(e)}"}))
        sys.exit(1)

    # If no videos are found in the playlist, exit the program.
    if not videos:
        print(json.dumps({"success": False, "error": "No videos found in the playlist."}))
        sys.exit(1)

    # Get the playlist name and create the folder for output.
    playlist_name = playlist_data.get('playlist_name', 'Unknown_Playlist')
    folder_path = os.path.join("Output", playlist_name)
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Generate the report in the requested format.
        if args.resultFormat == "cmd":
            playlist_table, video_table = compose_text_table(playlist_data, videos)
            print("Playlist Data:\n")
            print(playlist_table)
            print("\nVideo Data:\n")
        
        elif args.resultFormat == "txt":
            playlist_table, video_table = compose_text_table(playlist_data, videos)
            file_path = os.path.join(folder_path, f"{args.listMode}_{date_time}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"Playlist Data:\n\n{playlist_table}\n")
                file.write(f"\nVideo Data:\n\n{video_table}")
        
        elif args.resultFormat == "json":
            # Create a list of video data as dictionaries.
            videos_dict = []
            for video in videos:
                video_data = {
                    "title": getattr(video, 'title', 'N/A'),
                    "url": getattr(video, 'url', 'N/A'),
                    "duration": getattr(video, 'duration', 'N/A'),
                    "uploader": getattr(video, 'uploader', 'N/A'),
                    "uploader_url": getattr(video, 'uploader_url', 'N/A'),
                    "view_count": getattr(video, 'view_count', 'N/A'),
                    "valid": getattr(video, 'valid', 'N/A')
                }
                videos_dict.append(video_data)

            data_to_save = {
                "playlist_data": playlist_data,
                "videos": videos_dict
            }
            file_path = os.path.join(folder_path, f"{args.listMode}_{date_time}.json")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data_to_save, file, indent=4)

            print(json.dumps(data_to_save))
            return

        elif args.resultFormat == "csv":
            # Save the report as a CSV file.
            import csv
            file_path = os.path.join(folder_path, f"{args.listMode}_{date_time}.csv")
            with open(file_path, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                headers = ["Lp", "Title", "URL", "Duration", "Uploader", "Uploader URL", "Approximate View Count", "bValid"]
                writer.writerow(headers)

                for index, video in enumerate(videos):
                    writer.writerow([  # Write each video's data in a row.
                        index + 1,
                        getattr(video, 'title', 'N/A'),
                        getattr(video, 'url', 'N/A'),
                        getattr(video, 'duration', 'N/A'),
                        getattr(video, 'uploader', 'N/A'),
                        getattr(video, 'uploader_url', 'N/A'),
                        getattr(video, 'view_count', 'N/A'),
                        getattr(video, 'valid', 'N/A')
                    ])
        
        elif args.resultFormat == "html":
            # Generate an HTML report.
            js_code = open('web_template/script_head_template.js', 'r', encoding='utf-8').read()
            css_styles = open('web_template/style_template.css', 'r', encoding='utf-8').read()

            if args.listMode == "unavailable":
                html_list = generate_html_list_invalid_videos(videos, playlist_name, args.playlistLink)
                html_template_path = 'web_template/html_template_backup_removed_report.html'
                page_title = f"Removed videos for Playlist: {playlist_name}"
            else:
                html_list = generate_html_list(videos, playlist_name, args.playlistLink)
                html_template_path = 'web_template/html_template_backup_report.html'
                page_title = f"Report for Playlist: {playlist_name}"

            html_template = read_html_template(html_template_path)
            head, body = extract_head_and_body(html_template)

            # Final HTML content with embedded JavaScript and CSS.
            final_html = f"""<html>
            <head>
                <title>{page_title}</title>
                <script>{js_code}</script>
                <style>{css_styles}</style>
                {head}
            </head>
            <body>
                {body}
                {html_list}
                <footer>
                    <h3>Authors:</h3>
                    <div class='links'><a href='https://github.com/Kordight'><strong>Kordight</strong></a></div>
                </footer>
            </body>
            </html>"""

            # Save the HTML report to a file.
            file_path = os.path.join(folder_path, f"{args.listMode}_{date_time}.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(final_html)

        elif args.resultFormat == "mySQL":
            # Save the report to a MySQL database.
            db_config = load_db_config()
            create_database(db_config['host'], db_config['user'], db_config['password'], db_config['database'])
            add_report(
                db_config['host'], db_config['user'], db_config['password'], db_config['database'],
                [video.title for video in videos],
                [video.url for video in videos],
                playlist_name,
                args.playlistLink,
                [video.duration for video in videos],
                [video.uploader for video in videos],
                [video.uploader_url for video in videos],
                [video.view_count for video in videos],
                [video.valid for video in videos]
            )

        # If not JSON, print a success message.
        print(json.dumps({"success": True, "message": "Report generated successfully."}))

    except Exception as e:
        # Handle any errors during the report generation process.
        print(json.dumps({"success": False, "error": f"Processing error: {str(e)}"}))
        sys.exit(1)

# Entry point of the program.
if __name__ == "__main__":
    main()
