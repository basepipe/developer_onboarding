# encoding: utf-8
# module winsound
# from (pre-generated)
# by generator 1.147
"""
PlaySound(sound, flags) - play a sound
SND_FILENAME - sound is a wav file name
SND_ALIAS - sound is a registry sound association name
SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC
SND_MEMORY - sound is a memory image of a wav file
SND_PURGE - stop all instances of the specified sound
SND_ASYNC - PlaySound returns immediately
SND_NODEFAULT - Do not play a default beep if the sound can not be found
SND_NOSTOP - Do not interrupt any sounds currently playing
SND_NOWAIT - Return immediately if the sound driver is busy

Beep(frequency, duration) - Make a beep through the PC speaker.
"""
# no imports

# Variables with simple values

MB_ICONASTERISK = 64L
MB_ICONEXCLAMATION = 48L
MB_ICONHAND = 16L
MB_ICONQUESTION = 32L
MB_OK = 0L

SND_ALIAS = 65536L
SND_APPLICATION = 128L
SND_ASYNC = 1L
SND_FILENAME = 131072L
SND_LOOP = 8L
SND_MEMORY = 4L
SND_NODEFAULT = 2L
SND_NOSTOP = 16L
SND_NOWAIT = 8192L
SND_PURGE = 64L

# functions

def Beep(frequency, duration): # real signature unknown; restored from __doc__
    """
    Beep(frequency, duration) - a wrapper around the Windows Beep API
    
    The frequency argument specifies frequency, in hertz, of the sound.
    This parameter must be in the range 37 through 32,767.
    The duration argument specifies the number of milliseconds.
    """
    pass

def MessageBeep(x): # real signature unknown; restored from __doc__
    """ MessageBeep(x) - call Windows MessageBeep(x). x defaults to MB_OK. """
    pass

def PlaySound(sound, flags): # real signature unknown; restored from __doc__
    """
    PlaySound(sound, flags) - a wrapper around the Windows PlaySound API
    
    The sound argument can be a filename, data, or None.
    For flag values, ored together, see module documentation.
    """
    pass

# no classes
