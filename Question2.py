from moviepy import CompositeVideoClip, TextClip, VideoFileClip, concatenate_videoclips, vfx
from moviepy.video import *
import math
video = VideoFileClip("D:\Projects\FOG-Assessment\Tesla.mp4")
clips = [
    video.subclipped(26, 32).with_effects([vfx.CrossFadeOut(2)]),
    video.subclipped(96, 103).with_start(1).with_effects([vfx.CrossFadeIn(5)]),
    video.subclipped(98,101).with_effects([vfx.MirrorX()]),
    video.subclipped(91, 93).with_effects([vfx.MultiplySpeed(0.5)]).with_effects([vfx.CrossFadeIn(3)]),
]
final_clip = concatenate_videoclips(clips, method="compose")



# Add text overlay


final_clip.write_videofile("final_reel1.mp4", codec="libx264", fps=24)