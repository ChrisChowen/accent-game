"""Audio recording module for capturing voice samples."""

import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
from pathlib import Path
from typing import Optional


def record_audio(
    duration: float = 5.0,
    sample_rate: int = 16000,
    output_path: Optional[Path] = None
) -> Path:
    """
    Record audio from the default microphone.
    
    Args:
        duration: Recording duration in seconds
        sample_rate: Audio sample rate in Hz
        output_path: Path to save the audio file (defaults to tmp.wav)
        
    Returns:
        Path to the saved audio file
        
    Raises:
        RuntimeError: If recording fails
    """
    if output_path is None:
        output_path = Path("tmp.wav")
    
    try:
        print(f"Recording for {duration} seconds...")
        # Record audio as mono (channels=1)
        audio_data = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.float32
        )
        sd.wait()  # Wait until recording is finished
        
        # Convert to int16 for WAV format
        audio_int16 = (audio_data * 32767).astype(np.int16)
        
        # Save as WAV file
        wav.write(output_path, sample_rate, audio_int16)
        print(f"Audio saved to {output_path}")
        
        return output_path
        
    except Exception as e:
        raise RuntimeError(f"Failed to record audio: {e}") from e


if __name__ == "__main__":
    # Quick test - record 5 seconds and save to tmp.wav
    output_file = record_audio()
    print(f"Recording complete: {output_file}")
