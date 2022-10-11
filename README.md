# YourTTS: Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone


In our recent [paper](https://arxiv.org/abs/2112.02418) we propose the YourTTS model. YourTTS brings the power of a multilingual approach to the task of zero-shot multi-speaker TTS. Our method builds upon the VITS model and adds several novel modifications for zero-shot multi-speaker and multilingual training. We achieved state-of-the-art (SOTA) results in zero-shot multi-speaker TTS and results comparable to SOTA in zero-shot voice conversion on the VCTK dataset. Additionally, our approach achieves promising results in a target language with a single-speaker dataset, opening possibilities for zero-shot multi-speaker TTS and zero-shot voice conversion systems in low-resource languages. Finally, it is possible to fine-tune the YourTTS model with less than 1 minute of speech and achieve state-of-the-art results in voice similarity and with reasonable quality. This is important to allow synthesis for speakers with a very different voice or recording characteristics from those seen during training. 


## Production version
Come try our latest and greatest fullband english only model https://coqui.ai/

## Audios samples
Visit our [website](https://edresson.github.io/YourTTS/) for audio samples.

## Implementation
All of our experiments were implemented on the [Coqui TTS](https://github.com/coqui-ai/tts) repo.


## Colab Demos

| Demo                        | URL                                                                                            |
|-----------------------------|------------------------------------------------------------------------------------------------|
| Zero-Shot TTS               | [link](https://colab.research.google.com/drive/1WArisOG8vLGvrnoaLyEBOlJ0jG3LDtc2?usp=sharing)  |
| Zero-Shot VC                | [link](https://colab.research.google.com/drive/1gjdwOKCZuavPn_5oy8QA01sKmXpEq5AZ?usp=sharing) |
| Zero-Shot VC - Experiment 1 (trained with just VCTK)             | [link](https://colab.research.google.com/drive/1r0NDBxxW5RZjQ1Jy99XohnY6thYWNBCd?usp=sharing) |


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


## Coqui TTS released model
### TTS
To use the [🐸 TTS version v0.7.0](https://github.com/coqui-ai/TTS) released YourTTS model for Text-to-Speech use the following command: 
```
tts  --text "This is an example!" --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav target_speaker_wav.wav --language_idx "en"
```
Considering the "target_speaker_wav.wav" an audio sample from the target speaker.


### Voice conversion

To use the [🐸 TTS](https://github.com/coqui-ai/TTS) released YourTTS model for voice conversion use the following command: 

```
tts --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav target_speaker_wav.wav --reference_wav  target_content_wav.wav --language_idx "en"
```
Considering the "target_content_wav.wav" as the reference wave file to convert into the voice of the  "target_speaker_wav.wav" speaker.


## Results replicability

To insure replicability, we make the audios used to generate the MOS available [here](https://github.com/Edresson/YourTTS/releases/download/MOS/Audios_MOS.zip). In addition, we provide the MOS for each audio [here](https://github.com/Edresson/YourTTS/tree/main/metrics/MOS).

To re-generate our MOS results, follow the instructions [here](https://github.com/Edresson/YourTTS/tree/main/metrics/MOS). To predict the test sentences and generate the SECS, please use the Jupyter Notebooks available [here](https://github.com/Edresson/YourTTS/tree/main/metrics/SECS).
### Test Speakers:
  LibriTTS (test clean): 1188, 1995, 260, 1284, 2300, 237, 908, 1580, 121 and 1089
  
  VCTK: p261, p225, p294, p347, p238, p234, p248, p335, p245, p326 and p302
  
  MLS Portuguese:  12710, 5677, 12249, 12287, 9351, 11995, 7925, 3050, 4367 and 1306
  
  
## Reproducibility


The article was made using my Coqui TTS fork on the branch [multilingual-torchaudio-SE](https://github.com/Edresson/Coqui-TTS/tree/multilingual-torchaudio-SE/).


If you want to use the latest version of the  Coqui TTS you can get the config.json from the [Coqui released model](https://github.com/coqui-ai/TTS/releases/download/v0.5.0_models/tts_models--multilingual--multi-dataset--your_tts.zip). 


With config.json in hand, you first need to change the "datasets" configuration to your dataset. Using the config.json with the "datasets" configuration adjusted you need to extract the speaker's embeddings using our released speaker encoder using the following command:
`` python3 TTS/bin/compute_embeddings.py --model_path model_se.pth.tar --config_path  config_se.json --config_dataset_path  config.json --output_path d_vector_file.json`` 

"model_se.pth.tar" and "config_se.json" can be found in [Coqui released model](https://github.com/coqui-ai/TTS/releases/download/v0.5.0_models/tts_models--multilingual--multi-dataset--your_tts.zip) while config.json is the config you set the paths for.



Other parameters that you should change are on the "config.json":
  - "d_vector_file":  Now that you have the speaker embedding file (d_vector_file.json) adjust the "d_vector_file" parameter on the config setting to the path of the speaker embedding file.
  - "output_path": the path for saving the checkpoint and training logs
  - "speaker_encoder_config_path": The speaker encoder config to use to compute the speaker cosine similarity loss/speaker consistency loss ( set it to the config_se.json path)
  - "speaker_encoder_model_path": The speaker encoder checkpoint used to compute the speaker cosine similarity loss/speaker consistency loss ( set it to the "config_se.json" path)

Now that you have the config.json configured to replicate the training you can use the following command (if you like you can use the --restore_path {checkpoint_path} to do transfer learning from a checkpoint and speed up the training:
 `python3 TTS/bin/train_tts.py --config_path config.json`
 


## Citation

### Preprint

```

@ARTICLE{2021arXiv211202418C,
  author = {{Casanova}, Edresson and {Weber}, Julian and {Shulby}, Christopher and {Junior}, Arnaldo Candido and {G{\"o}lge}, Eren and {Antonelli Ponti}, Moacir},
  title = "{YourTTS: Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone}",
  journal = {arXiv e-prints},
  keywords = {Computer Science - Sound, Computer Science - Computation and Language, Electrical Engineering and Systems Science - Audio and Speech Processing},
  year = 2021,
  month = dec,
  eid = {arXiv:2112.02418},
  pages = {arXiv:2112.02418},
  archivePrefix = {arXiv},
  eprint = {2112.02418},
  primaryClass = {cs.SD},
  adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv211202418C},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

```

### Published paper at ICML
```
@inproceedings{casanova2022yourtts,
  title={Yourtts: Towards zero-shot multi-speaker tts and zero-shot voice conversion for everyone},
  author={Casanova, Edresson and Weber, Julian and Shulby, Christopher D and Junior, Arnaldo Candido and G{\"o}lge, Eren and Ponti, Moacir A},
  booktitle={International Conference on Machine Learning},
  pages={2709--2720},
  year={2022},
  organization={PMLR}
}

```
