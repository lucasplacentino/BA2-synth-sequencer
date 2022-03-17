
# * Global variables:

# Saved sequence file path
SAVE_FILE = "/path/to/saved-sequence-file.txt"

# Simulated DAC
SIMULATED_DAC = False

# Simulated LCD
SIMULATED_LCD = False

# PITCH
MAX_PITCH = 12
MIN_PITCH = 1

# OCTAVE
MAX_OCTAVE = 2  # 4 when 5V, here only 2 because only 3.3V
MIN_OCTAVE = 0

NB_NOTES = MAX_PITCH*(MAX_OCTAVE+1)

# STEP
NB_STEPS = 8
#MAX_STEP = 7
MAX_STEP = NB_STEPS-1
MIN_STEP = 0

# DAC
PITCH_CHANNEL = 0 #dac 1
GATE_CHANNEL = 0 #dac 2
CV1_CHANNEL = 1 #dac 2
CV2_CHANNEL = 0 #dac 3
CV3_CHANNEL = 1 #dac 3
MAX_DAC = 4095 # 12bit

# CV
MAX_CV = 25
MIN_CV = 0

# TEMPO (BPM)
MAX_TEMPO = 359
MIN_TEMPO = 2

# LED_QUANTITY
LED_QUANTITY = 8
