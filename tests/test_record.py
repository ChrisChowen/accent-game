"""Test module for audio recording functionality."""

import pytest
from unittest.mock import patch, MagicMock
import numpy as np
from pathlib import Path
import tempfile
import os

from accent_game.record import record_audio


class TestRecordAudio:
    """Test cases for the record_audio function."""
    
    @patch('accent_game.record.sd.rec')
    @patch('accent_game.record.sd.wait')
    @patch('accent_game.record.wav.write')
    def test_record_audio_default_params(self, mock_wav_write, mock_wait, mock_rec):
        """Test recording with default parameters."""
        # Mock the recorded audio data
        mock_audio = np.random.rand(80000, 1).astype(np.float32)  # 5s * 16kHz
        mock_rec.return_value = mock_audio
        
        # Call the function
        result_path = record_audio()
        
        # Verify calls
        mock_rec.assert_called_once_with(80000, samplerate=16000, channels=1, dtype=np.float32)
        mock_wait.assert_called_once()
        mock_wav_write.assert_called_once()
        
        # Check return value
        assert result_path == Path("tmp.wav")
    
    @patch('accent_game.record.sd.rec')
    @patch('accent_game.record.sd.wait')
    @patch('accent_game.record.wav.write')
    def test_record_audio_custom_params(self, mock_wav_write, mock_wait, mock_rec):
        """Test recording with custom parameters."""
        # Mock the recorded audio data
        mock_audio = np.random.rand(48000, 1).astype(np.float32)  # 3s * 16kHz
        mock_rec.return_value = mock_audio
        
        custom_path = Path("test_audio.wav")
        
        # Call with custom parameters
        result_path = record_audio(duration=3.0, sample_rate=16000, output_path=custom_path)
        
        # Verify calls
        mock_rec.assert_called_once_with(48000, samplerate=16000, channels=1, dtype=np.float32)
        mock_wait.assert_called_once()
        mock_wav_write.assert_called_once()
        
        # Check return value
        assert result_path == custom_path
    
    @patch('accent_game.record.sd.rec')
    def test_record_audio_failure(self, mock_rec):
        """Test recording failure handling."""
        # Mock recording failure
        mock_rec.side_effect = Exception("Microphone not available")
        
        # Should raise RuntimeError
        with pytest.raises(RuntimeError, match="Failed to record audio"):
            record_audio()
    
    @patch('accent_game.record.sd.rec')
    @patch('accent_game.record.sd.wait')
    @patch('accent_game.record.wav.write')
    def test_audio_conversion_to_int16(self, mock_wav_write, mock_wait, mock_rec):
        """Test that audio data is properly converted to int16."""
        # Create known float32 audio data
        mock_audio = np.array([[0.5], [-0.5], [1.0], [-1.0]], dtype=np.float32)
        mock_rec.return_value = mock_audio
        
        record_audio(duration=0.001)  # Very short duration
        
        # Check that wav.write was called with int16 data
        call_args = mock_wav_write.call_args
        written_data = call_args[0][2]  # Third argument is the audio data
        
        assert written_data.dtype == np.int16
        # Check approximate conversion (0.5 * 32767 ≈ 16383)
        expected = np.array([16383, -16383, 32767, -32767], dtype=np.int16).reshape(-1, 1)
        np.testing.assert_array_almost_equal(written_data, expected, decimal=0)
