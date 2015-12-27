class cls(object):
    def __repr__(self):
        import os
        os.system( 'cls' if os.name == 'nt' else 'clear')
        return ''

    cls = cls()
        
