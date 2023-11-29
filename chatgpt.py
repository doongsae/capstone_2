import sounddevice as sd
import numpy as np
import time
from scipy.io.wavfile import read
from transformers import pipeline
import nlptutti as metrics
import wavio

## Mic channel 1 기준. 2라면 아래 channels를 2로 바꿔주면 된다.
pipe = pipeline(model="doongsae/whisper_finetuning")


def read_wav_file(filename):
    fs, data = read(filename)
    return fs, data
    

def record_audio(duration, filename):
    # 마이크에서 오디오 데이터를 기록
    fs = 44100  # 샘플링 속도 (Hz)
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype=np.float32)
    sd.wait()

    # 기록된 오디오 데이터를 WAV 파일로 저장
    wavio.write(filename, recording, fs, sampwidth=2)

    
def calc():
    # 사용 예시
    filename = "output.wav"  # 실제 파일 이름으로 변경해야 합니다.
    res = pipe(filename)["text"]
    
    words = ["살려줘", "구해줘", "일일구 불러줘", "긴급 에스오에스", "도와줘", "긴급알림해줘"]
    flgs = 0
    rr = 0.0
    
    print(res)

    for idx in words:
        if (metrics.get_cer(idx, res)['cer'] < 0.1):
            rr = metrics.get_cer(idx, res)['cer']
            flgs = 1

    if flgs == 1:
        return "Detected"
    else:
        return "X"


def main():
    # 데시벨 임계값 설정 > 기존 60
    threshold_db = 35

    while True:
        # 마이크 입력 모니터링
        duration = 0.01  # 녹음할 시간 (초)

        # 마이크 입력 받기
        audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
        sd.wait()

        # 데시벨 계산
        rms = np.sqrt(np.mean(audio_data**2))
        current_db = 20 * np.log10(rms)

        print(f"Current Decibel Level: {current_db:.2f} dB")

        # 데시벨이 임계값을 초과하면 녹음 시작
        if current_db > threshold_db:
            print("Decibel threshold exceeded. Recording for 5 seconds...")
            filename = "output.wav"
            record_audio(3, filename)
            print(f"Recording saved as {filename}\n")
            print(calc())


if __name__ == "__main__":
    main()
