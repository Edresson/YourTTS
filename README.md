# YourTTS: Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone


In our recent [paper]() we propose the YourTTS model. YourTTS brings the power of a multilingual approach to the task of zero-shot multi-speaker TTS. Our method builds upon the VITS model and adds several novel modifications for zero-shot multi-speaker and multilingual training. We achieved state-of-the-art (SOTA) results in zero-shot multi-speaker TTS and results comparable to SOTA in zero-shot voice conversion on the VCTK dataset. Additionally, our approach achieves promising results in a target language with a single-speaker dataset, opening possibilities for zero-shot multi-speaker TTS and zero-shot voice conversion systems in low-resource languages. Finally, it is possible to fine-tune the YourTTS model with less than 1 minute of speech and achieve state-of-the-art results in voice similarity and with reasonable quality. This is important to allow synthesis for speakers with a very different voice or recording characteristics from those seen during training. 



## Audios samples
Visit our [website](https://edresson.github.io/YourTTS/) for audio samples.

## Implementation
All of our experiments were implemented at [Coqui TTS](https://github.com/coqui-ai/tts).


## Colab Demos



## Checkpoints

All the released checkpoints are licensed under CC BY-NC-ND 4.0

| Model                        | URL                                                                                            |
|------------------------------|------------------------------------------------------------------------------------------------|
| Speaker Encoder              | [link](https://drive.google.com/drive/folders/1WKK70aBnA-ZI2Z1Ka_zWgBK7O0Y3TLey?usp=sharing)   |
| Exp 1. YourTTS-EN(VCTK)         | [link](https://drive.google.com/drive/folders/15MfBCRyM8ViZ5Ghe16bGz0UtB_O0iovX?usp=sharing)   |
| Exp 1. YourTTS-EN(VCTK)  + SCL         | [link](https://drive.google.com/drive/folders/10hX5B_h0dzroY7bVNPodC8hzhz4nklzR?usp=sharing)   |
| Exp 2. YourTTS-EN(VCTK)-PT          | [link](https://drive.google.com/drive/folders/1Mdob20nFQEKUwavw_DhqMc1MfG3CNNNI?usp=sharing) |
| Exp 2. YourTTS-EN(VCTK)-PT  + SCL   | [link](https://drive.google.com/drive/folders/1uorMp_A0LNEfwdkM1QB9jz4Mf3kM5sGn?usp=sharing) |
| Exp 3. YourTTS-EN(VCTK)-PT-FR       | [link](https://drive.google.com/drive/folders/15NAhIeHXJZLxrZMoCaUlH_7mS7TRqdme?usp=sharing) |
| Exp 3. YourTTS-EN(VCTK)-PT-FR SCL   | [link](https://drive.google.com/drive/folders/1H7VrW6eUO0wle-e6Un3mp77udkZLMrMr?usp=sharing) |
| Exp 4. YourTTS-EN(VCTK+LibriTTS)-PT-FR SCL | [link](https://drive.google.com/drive/folders/15G-QS5tYQPkqiXfAdialJjmuqZV0azQV?usp=sharing) |


## Results replicability

To replicability we make the audios used to calculate the MOS available [here](https://github.com/Edresson/YourTTS/releases/download/MOS/Audios_MOS.zip). In addition, we provide the Mean Opinion scores for each audio [here](https://github.com/Edresson/YourTTS/tree/main/metrics/MOS).

To recompute our MOS results follow the instructions [here](https://github.com/Edresson/YourTTS/tree/main/metrics/MOS). To predict the test sequences and compute the SECS results, please use the Jupyter Notebooks available [here](https://github.com/Edresson/YourTTS/tree/main/metrics/SECS).

