class LineProcessor():
    '''This class generically processes a series of strings one at a time.

    This is designed to support the KSPDataReader.
    '''
    def __init__(self, rules):
        '''Set up the LineProcessor with it's rules table.

        rules should be a sequence of (RE pattern, callable) pairs.
        '''
        self.rules = rules

    def process_line(self, line):
        '''Dispatch this line to a handler according to the rules table.

        The rules in the rules table are tested in order. On the first
        match, the match object is passed to the associated handler.
        '''
        for pattern, handler in self.rules:
            match = pattern.match(line)
            if match:
                print('handled by ', handler)
                handler(match)
                break
