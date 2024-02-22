import json
import os

# Define the HTML content with appropriate spacing
html_content = '''
<!DOCTYPE html>
<html>
  <head>
    <meta property="og:image" content="{thumbnail_link}">
    <meta property="og:type" content="video.other">
    
    <meta property="og:video:url" content="{link}">
    <meta property="og:video:height" content="720">
    <meta property="og:video:width" content="1280">
    
    <meta http-equiv="refresh" content="0; url=https://pokermmon.github.io/" />
  </head>
  <body>
  </body>
</html>
'''

# Define the index.html content for JN, EN_S, and EN_D directories
index_html_content = '''
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=https://pokermmon.github.io/episodes" />
</head>
<body>
</body>
</html>
'''

# Define the index.html content for the specified folder directory
main_index_html_content = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Episode Parser</title>
  <style>
    body {
      background-color: black;
      color: white; /* Set text color to white for contrast */
    }
  </style>
</head>
<body>
  If you want to watch an episode via this method, format the link like this in a messaging service:<br>https://pokermmon.github.io/episodes/JP (OR) EN_S (OR) EN_D/#
</body>
</html>
'''

def create_folders_and_html():
    txt_file_directory = input("Please input the directory of the txt file: ")
    folder_directory = input("Please input the directory of the folder where you want to create subfolders: ")
    
    with open(txt_file_directory, "r") as file:
        data = json.load(file)
    
    episodes = data["episodes"]
    
    # Create the specified folder directory if it doesn't exist
    if not os.path.exists(folder_directory):
        os.makedirs(folder_directory)
    
    # Create index.html in the specified folder directory
    main_index_folder_path = os.path.join(folder_directory, "index.html")
    with open(main_index_folder_path, "w") as main_index_html_file:
        main_index_html_file.write(main_index_html_content)
    
    for directory in ["JN", "EN_S", "EN_D"]:
        # Create index.html in JN, EN_S, and EN_D directories
        index_folder_path = os.path.join(folder_directory, directory)
        index_html_path = os.path.join(index_folder_path, "index.html")
        if not os.path.exists(index_folder_path):
            os.makedirs(index_folder_path)
        with open(index_html_path, "w") as index_html_file:
            index_html_file.write(index_html_content)
        
        for episode in episodes:
            number = episode["number"]
            link = episode[directory]
            thumbnail_link = episode["JN_T"] if directory in ["JN", "EN_S"] else episode["EN_T"]
            if link == "N/A":
                link = "/assets/none.mp4"
            if thumbnail_link == "N/A":
                thumbnail_link = "/assets/none.jpg"
            folder_path = os.path.join(folder_directory, directory, number)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Use the pre-defined html_content with proper spacing
            formatted_html_content = html_content.format(thumbnail_link=thumbnail_link, link=link)
            episode_html_path = os.path.join(folder_path, "index.html")
            with open(episode_html_path, "w") as html_file:
                html_file.write(formatted_html_content)

if __name__ == "__main__":
    create_folders_and_html()