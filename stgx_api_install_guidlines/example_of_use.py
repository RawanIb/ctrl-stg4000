from stg.api import PulseFile, STG4000

stg = STG4000()
stg.download(0, *PulseFile().compile())
stg.start_stimulation([0])