# awgn_sim.py
import numpy as np
from sionna import utils

def snr_to_noise_variance(snr_db, signal_power=1.0):
    snr_linear = 10**(snr_db / 10)
    return signal_power / snr_linear

def run_awgn_experiment(num_bits=1000, snr_db=10):

    # Generate random bits {0,1}
    bits_tx = np.random.randint(0, 2, size=(num_bits,))

    # BPSK mapping: 0 -> -1, 1 -> +1
    x = 2*bits_tx - 1

    # Convert SNR(dB) to noise variance
    noise_var = snr_to_noise_variance(snr_db, 1.0)  
    # We assume signal power = 1.0

    # Generate AWGN
    noise = np.sqrt(noise_var/2) * np.random.randn(num_bits)

    # Received signal
    y = x + noise

    # BPSK demapping: decide if y > 0 -> 1 else 0
    bits_rx = (y > 0).astype(np.int32)

    # Compute BER
    bit_errors = np.sum(bits_tx != bits_rx)
    ber = bit_errors / num_bits
    return ber
