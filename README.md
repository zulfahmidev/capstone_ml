![Logo Transparent white](https://github.com/zulfahmidev/capstone_ml/blob/6298e28afa35ab2c73baefb64e965ab6c97a621d/src/public/Arahku-removebg-preview.png)

# Introduction

This project is built with the aim of helping students make informed decisions when it comes to choosing their college majors. Many students make the wrong choices by relying on unverified information from the [internet](https://www.detik.com/edu/detikpedia/d-5828770/87-persen-mahasiswa-ri-merasa-salah-jurusan-apa-sebabnya), without realizing that the decision is more complex than that. Additionally, factors such as peer pressure, the desire to prove oneself, environmental influences, parental pressure, and more contribute to this issue. 

The advantages of this application lie in its features that include talent interest tests, brain preference tests, major suitability tests, major recommendations, and recommendations from close friends. All of these features are supported by machine learning technology and cloud computing. The hope is that this application can serve as a safe and reliable source of information for students before they make decisions about their college majors and plan their future.


# Prerequisites

* scikit-learn 1.2.2
* numpy 1.23.5
* pandas 2.0.1

# Quick Start

# 1. Get the Repo

Simply run the commands below:

```
git clone https://github.com/pytorch/ios-demo-app
cd ios-demo-app/SpeechRecognition
```

If you don't have PyTorch 1.10 and torchaudio 0.10 installed or want to have a quick try of the demo app, you can download the quantized scripted wav2vec2 model file [here](https://pytorch-mobile-demo-apps.s3.us-east-2.amazonaws.com/wav2vec2.ptl), then drag and drop to the project, and continue to Step 3.

## 2. Prepare the Model

To install PyTorch 1.10, torchaudio 0.10 and the Hugging Face transformers, you can do something like this:

```
conda create -n wav2vec2 python=3.8.5
conda activate wav2vec2
pip install torch torchaudio
pip install transformers
```

Now with PyTorch 1.10 and torchaudio 0.10 installed, run the following commands on a Terminal:

```
python create_wav2vec2.py
```

This will create the model file `wav2vec2.ptl` and save to the `SpeechRecognition` folder.

## 2. Use LibTorch

Run the commands below:

```
pod install
open SpeechRecognition.xcworkspace/
```

### 3. Build and run with Xcode

After the app runs, tap the Start button and start saying something; after 12 seconds (you can change `private let AUDIO_LEN_IN_SECOND = 12` in `ViewController.swift` for a longer or shorter recording length), the model will infer to recognize your speech. Some example results are as follows:
