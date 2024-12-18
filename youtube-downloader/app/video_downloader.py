from pytube import YouTube

yt_download_object = YouTube("https://www.youtube.com/watch?v=rGX1Ch6OyUs")

"""
There might be an issue related to cipher 'pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple'
Fix can be found here: https://github.com/pytube/pytube/issues/1750#issuecomment-1672185669
"""

stream_list = yt_download_object.streams

"""
You may notice that some streams listed have both a video codec and audio codec, while others have just video or just audio, 
this is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH).
"""

# print(stream_list.filter(type="audio"))
# print(stream_list.filter(file_extension='mp4'))

# Download the video by itag
# single_stream = stream_list.get_by_itag(271)
# single_stream.download(output_path=".//vyd//downloads", filename="video.mp4")
single_stream = stream_list.get_by_itag(251)
single_stream.download(output_path=".//vyd//downloads", filename="audio.mp4")
