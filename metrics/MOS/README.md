# YourTTS MOS and Sim-MOS

## MOS samples
You can download the MOS and Sim-MOS samples in: https://github.com/Edresson/YourTTS/releases/download/MOS/Audios_MOS.zip

## MOS/Sim-MOS per audio
You can check the MOS for each Audio for English in the "EN/" directory, for Portuguese in the "PT/" directory and for the experiment that was 
evaluated with annotators of both languages in "EN-PT/".

## Recompute MOS/Sim-MOS

You can recalculate the MOS with their respective confidence intervals for the English language using the bellow command:

    python3 compute_similarity_MOS.py --csv_path EN/naturalness-MOS.csv

And Sim-MOS using the command:

    python3 compute_similarity_MOS.py --csv_path EN/Sim-MOS.csv 
