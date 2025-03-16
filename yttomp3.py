# import streamlit as st
# import os
# import yt_dlp
# from pathlib import Path
# import shutil

# # Set up directory for storing audio files
# PLAYLIST_DIR = "playlist"
# if not os.path.exists(PLAYLIST_DIR):
#     os.makedirs(PLAYLIST_DIR)

# # Function to download YouTube audio without FFmpeg
# def download_song(yt_url, output_path=PLAYLIST_DIR):
#     try:
#         ydl_opts = {
#             'format': 'bestaudio/best',  # Get the best audio available
#             'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
#             'quiet': True,
#             # No postprocessing, just download the audio as-is (usually M4A)
#         }
        
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(yt_url, download=True)
#             # Get the downloaded file path
#             downloaded_file = ydl.prepare_filename(info)
#             # Optionally rename to .mp3 extension (no conversion, just renaming)
#             if downloaded_file.endswith('.m4a'):
#                 new_file = downloaded_file.replace('.m4a', '.mp3')
#                 os.rename(downloaded_file, new_file)
#                 return new_file
#             return downloaded_file
#         return True
#     except Exception as e:
#         st.error(f"Error downloading song: {str(e)}")
#         return False

# # Function to get list of audio files in playlist
# def get_playlist_songs():
#     return [f for f in os.listdir(PLAYLIST_DIR) if f.endswith(('.mp3', '.m4a','.webm'))]

# # Main Streamlit app
# def main():
#     st.title("YouTube to Audio Playlist Converter (No FFmpeg)")
    
#     # Input for YouTube URL
#     yt_url = st.text_input("Enter YouTube Song URL", "")
    
#     # Download button
#     if st.button("Download Audio"):
#         if yt_url:
#             with st.spinner("Downloading audio..."):
#                 result = download_song(yt_url)
#                 if result:
#                     st.success("Audio downloaded successfully!")
#         else:
#             st.warning("Please enter a YouTube URL")
    
#     # Playlist section
#     st.subheader("Your Playlist")
#     playlist = get_playlist_songs()
    
#     if playlist:
#         # Display playlist
#         selected_song = st.selectbox("Select a song to play", playlist)
        
#         # Audio player
#         song_path = os.path.join(PLAYLIST_DIR, selected_song)
#         audio_file = open(song_path, 'rb')
#         audio_bytes = audio_file.read()
#         st.audio(audio_bytes, format='audio/mp3')  # Works with M4A too
        
#         # Option to clear playlist
#         if st.button("Clear Playlist"):
#             shutil.rmtree(PLAYLIST_DIR)
#             os.makedirs(PLAYLIST_DIR)
#             st.success("Playlist cleared!")
#             st.experimental_rerun()
#     else:
#         st.write("Your playlist is empty. Add some songs!")

# if __name__ == "__main__":
#     # Dependencies info
#     st.sidebar.title("About")
#     st.sidebar.info(
#         "This app downloads YouTube audio without FFmpeg.\n\n"
#         "Dependencies:\n"
#         "- streamlit\n"
#         "- yt-dlp\n"
#         "Note: Audio will be in M4A format (renamed to MP3)"
#     )
    
#     main()

import streamlit as st
import os
import yt_dlp
from pathlib import Path
import shutil

# Set up directory for storing audio files
PLAYLIST_DIR = "playlist"
if not os.path.exists(PLAYLIST_DIR):
    os.makedirs(PLAYLIST_DIR)

# Function to download YouTube audio without FFmpeg
def download_song(yt_url, output_path=PLAYLIST_DIR):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Get the best audio available
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': True,
            # No postprocessing, just download the audio as-is (usually M4A)
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url, download=True)
            # Get the downloaded file path
            downloaded_file = ydl.prepare_filename(info)
            # Optionally rename to .mp3 extension (no conversion, just renaming)
            if downloaded_file.endswith('.m4a'):
                new_file = downloaded_file.replace('.m4a', '.mp3')
                os.rename(downloaded_file, new_file)
                return new_file
            return downloaded_file
        return True
    except Exception as e:
        st.error(f"Error downloading song: {str(e)}")
        return False

# Function to get list of audio files in playlist
def get_playlist_songs():
    return [f for f in os.listdir(PLAYLIST_DIR) if f.endswith(('.mp3', '.m4a','.webm'))]

# Main Streamlit app
def main():
    st.title("YouTube to Audio Playlist Converter (No FFmpeg)")

    # Input for YouTube URL
    yt_url = st.text_input("Enter YouTube Song URL", "")

    # Download button
    if st.button("Download Audio"):
        if yt_url:
            with st.spinner("Downloading audio..."):
                result = download_song(yt_url)
                if result:
                    st.success("Audio downloaded successfully!")
        else:
            st.warning("Please enter a YouTube URL")

    # Playlist section
    st.subheader("Your Playlist")
    playlist = get_playlist_songs()

    if playlist:
        # Display playlist with audio player and song names
        st.write("Playlist:")
        for song in playlist:
            song_path = os.path.join(PLAYLIST_DIR, song)
            audio_file = open(song_path, 'rb')
            audio_bytes = audio_file.read()
            st.markdown(f"**Song:** {song}")  # Display the song name
            st.audio(audio_bytes, format='audio/mp3', start_time=0)  # Works with M4A too

        # Option to clear playlist
        if st.button("Clear Playlist"):
            shutil.rmtree(PLAYLIST_DIR)
            os.makedirs(PLAYLIST_DIR)
            st.success("Playlist cleared!")
            st.experimental_rerun()
    else:
        st.write("Your playlist is empty. Add some songs!")

if __name__ == "__main__":
    # Dependencies info
    st.sidebar.title("About")
    st.sidebar.info(
        "This app downloads YouTube audio without FFmpeg.\n\n"
        "Dependencies:\n"
        "- streamlit\n"
        "- yt-dlp\n"
        "Note: Audio will be in M4A format (renamed to MP3)"
    )

    main()
