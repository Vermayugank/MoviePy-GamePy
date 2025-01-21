from moviepy import VideoFileClip, concatenate_videoclips, TextClip, vfx, ImageSequenceClip, AudioFileClip
import cv2

def applyTransitions(video):
    # Create subclips and apply effects
    clips = [
        video.subclipped(26, 32).with_effects([vfx.CrossFadeOut(2)]), # crossFade Effect
        video.subclipped(96, 103).with_start(1).with_effects([vfx.CrossFadeIn(5)]), #CrossFadeIn Effect
        video.subclipped(98,101).with_effects([vfx.MirrorX()]),
        video.subclipped(91, 93).with_effects([vfx.MultiplySpeed(0.5)]).with_effects([vfx.CrossFadeIn(3)]), #Slow down the clip spedd with CrossFadeIn effct
    ]
    # Concatenate the clips
    final_clip = concatenate_videoclips(clips, method="compose")
    return final_clip

def applyTextOverlay(frames, text, display_duration=4, fps=30):
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 5
    thickness = 8
    padding = 25
    total_frames = len(frames)
    display_frames = display_duration * fps

    for i in range(total_frames):
        frame = frames[i]
        frame_height, frame_width = frame.shape[:2]

        if i < display_frames:
            textsize = cv2.getTextSize(text, font, font_scale, thickness)[0]
            textX = (frame_width - textsize[0]) // 2
            textY = (frame_height + textsize[1]) // 2

            # Calculate fade-in and fade-out effect
            alpha = 1.0
            if i < fps:  # Fade-in effect
                alpha = i / float(fps)
            elif i > display_frames - fps:  # Fade-out effect
                alpha = (display_frames - i) / float(fps)

            overlay = frame.copy()
            cv2.putText(overlay, text, (textX, textY + 400), font, font_scale, (0, 0, 0), thickness)
            cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    return frames

# Main function to process video
def addText(clip, descriptive_text):
    frames = []
    for frame in clip.iter_frames():
        frames.append(frame)
    frames_with_text = applyTextOverlay(frames, descriptive_text)
    frames_with_text = ImageSequenceClip(frames_with_text, fps=clip.fps)
    return frames_with_text

if __name__ == "__main__":
    # Load the video
    video = VideoFileClip("./Tesla.mp4")
    final_clip = applyTransitions(video)
    final_clip_with_text = addText(final_clip, "Tesla Highlights")

    # Add background music
    # audio = AudioFileClip("background.wav")
    # final_clip_with_audio = final_clip_with_text.set_audio(audio)

    final_clip_with_text.write_videofile("final_reel2.mp4", codec="libx264", fps=24)
