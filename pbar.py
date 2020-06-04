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
    '''
    pbar = ProgressBar(widgets=widgets)
    return pbar
