class LineProcessor():
    '''This class generically processes a series of strings one at a time.

    This is designed to support the KSPDataReader.
    '''
    def __init__(self, rules):
        '''Set up the LineProcessor with it's rules table.

        rules should be a sequence of (RE pattern, callable) pairs.
        '''
        self.rules = rules

    def dispatch_line(self, line):
        '''Dispatch this line to a handler according to the rules table.

        The rules in the rules table are tested in order. On the first
        match, the match object is passed to the associated handler.

        If there are no matches, this will raise an UnexpectedLineError.
        To prevent this behavior, add a super-permissive rule with a noop
        handler.
        '''
        for pattern, handler in self.rules:
            match = pattern.match(line)
            if match:
                handler(match)
                break
        else:
            raise UnexpectedLineError('encountered a line that did not match any rules', line)

    def process_lines(self, lines):
        for i, line in enumerate(lines):
            try:
                self.dispatch_line(line)
            except UnexpectedLineError as e:
                e.line_number = i+1
                print('''Encountered a line that did not match any rules.
Line number: {}
Line: "{}"
                      '''.format(e.line_number, e.line))
                raise


class UnexpectedLineError(ValueError):
    def __init__(self, message=None, line=None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.line = line

    def __repr__(self):
        class_name = type(self).__name__
        return '{}: Line {} ("{}") did not match any rules.'.format(class_name,
                                                                    self.line_number,
                                                                    self.line)

    line_number = None
    line = None
