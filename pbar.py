from os import system
try:
    from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
        AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
        ProgressBar, ReverseBar, RotatingMarker, \
        SimpleProgress, Timer
except:
    cmd = 'pip install progressbar'
    blah = input('Installing pbar...(press ctrl+c to quit)')
    system(cmd)
    from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
        AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
        ProgressBar, ReverseBar, RotatingMarker, \
        SimpleProgress, Timer        
        
       

widgets = [Percentage(), 
        ' ', Bar(),
        ' ', ETA(),
        ' ', AdaptiveETA()]

def get_pbar():
    '''
    uses https://pypi.org/project/progressbar/#files
    Usage:
    for x in pbar(my_list):
        ...
    '''
    pbar = ProgressBar(widgets=widgets)
    return pbar
