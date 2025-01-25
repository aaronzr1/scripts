#!/bin/bash

video_name = my-video
ffmpeg -i "${video_name}.mov" -vcodec h264 -acodec mp2 "${video_name}.mp4"