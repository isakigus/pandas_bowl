class League:
    def __init__(self):
        self.title = ''
        self.folder = ''
        self.period = ''
        self.img = ''
        self.comment = ''
        self.background = 'black'


tiburon = League()
tiburon.title = 'Tiburon Negro'
tiburon.img = 'white_shark.png'
tiburon.folder = 'tiburon_negro'
tiburon.period = 'Septiembre - Octubre 2020'
tiburon.comment = 'La liga del tiburón'
tiburon.background = 'black'

delfin = League()
delfin.title = 'Delfín Rojo'
delfin.img = 'dolphin-2-xxl.png'
delfin.folder = 'delfin_rojo'
delfin.period = 'Octubre - Diciembre 2020'
delfin.comment = 'La liga del delfín sin fín'
delfin.background = '#734e4e'


leagues = [tiburon, delfin]
