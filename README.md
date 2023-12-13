# Capstone Design II, Sogang University

Speech recognition with Sounddevice / Huggingface in Capstone Design Projects


## Inference

```shell
git clone https://github.com/doongsae/capstone_2.git

# on Ubuntu
sudo apt install ffmpeg

pip install requirements.txt

python chatgpt.py
```


## Model
Baseline model: [OpenAI Whisper](https://github.com/openai/whisper) [Base model]

Fine-tuning with Huggingface - Trainer with TTS dataset
```
https://huggingface.co/doongsae/whisper_finetuning
```

## Training
### Datasets
15 minutes dataset from TTS / recording

6 words: [살려줘, 구해줘, 도와줘, 119 불러줘, 긴급 알림 해줘, 긴급 SOS]

#### Using TTS service
- [Clova Dubbing](https://clovadubbing.naver.com/)
- [Typecast AI](https://www.typecast.ai)
<br/><br/>


### Training Results
Character Error Rate (CER): calculate with [Nlptutti](https://pypi.org/project/nlptutti/)

![다운로드](https://github.com/doongsae/capstone_2/assets/51825988/2dab17fa-a212-4c04-a1d3-4ac09cc0ce88)
<br/><br/>

## External Links
### Reference
- [HuggingFace Transformer Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer)
- [Whisper Fine-tuning Tutorial](https://huggingface.co/blog/fine-tune-whisper)

#### Capstone Design Wiki
- [Sogang University Capstone Design II Wiki](http://cscp2.sogang.ac.kr/CSE4187/index.php/%EC%A1%B8%EC%97%85%ED%95%98%EB%9F%AC%EA%B0%91%EB%8B%88%EB%8B%A4)
