import sounddevice as sd
import scipy.io.wavfile as wav

from pygame import*

fs = 44100
recording = None
is_recording = False
voice_file= 'voice_record.wav'
minus_track = 'смарагдове небо.mp3'


init()
mixer.music.set_volume(0.5)
win_size = 1000,800
win = display.set_mode(win_size)
clock = time.Clock()
font.init()
font_big = font.SysFont('Arial',32)
btn_rect = Rect(200,150,200,80)
rect_color = 'white'
btn_text = 'запис'

seconds = 180

def start_voise_record():
    global recording
    recording = sd.rec(int(seconds*fs),samplerate=fs,channels=1,dtype='int16')

def stop_voise_record():
    global recording
    voise_sound.stop()
    sd.stop
    if recording is not None:
        wav.write(voice_file,fs,recording)
        
def play_song_and_voice_together():
    try:
        voise_sound.stop()
    except:
        pass
    mixer.music.load(minus_track)
    mixer.music.play()
    voise_sound = mixer.Sound(voice_file)
    voise_sound.play()


play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False
        if e.type == MOUSEBUTTONDOWN:
            if btn_rect.collidepoint(e.pos):
                if not is_recording:
                    rect_color = 'red'
                    btn_text = 'стоп та прослухати'
                    is_recording = True
                    voise_sound = mixer.Sound(minus_track)
                    voise_sound.play()
                    start_voise_record()
                else:
                    rect_color = 'white'
                    btn_text = 'запис'
                    is_recording = False
                    stop_voise_record()
                    play_song_and_voice_together()

    win.fill('grey')
    draw.rect(win,rect_color,btn_rect)
    text_serface = font_big.render(btn_text,True,'black')
    win.blit(text_serface,(btn_rect.x + 20,btn_rect.y + 20))

    
    display.update()
    clock.tick(60)
