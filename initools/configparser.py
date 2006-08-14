"""
This implements the public `ConfigParser` interface, but with some
additional enhancements.

These are:


"""

class NoSectionError(Exception):
    """Exception raised when a specified section is not found."""

class DuplicateSectionError(Exception):
    """Exception raised if add_section() is called with the name of a
    section that is already present."""

class NoOptionError(Exception):
    """Exception raised when a specified option is not found in the
    specified section."""

class InterpolationError(Exception):
    """Base class for exceptions raised when problems occur performing
    string interpolation."""

class InterpolationDepthError(Exception):
    """Exception raised when string interpolation cannot be completed
    because the number of iterations exceeds
    MAX_INTERPOLATION_DEPTH. Subclass of InterpolationError."""

class InterpolationMissingOptionError(Exception):
    """Exception raised when an option referenced from a value does
    not exist. Subclass of InterpolationError."""

class InterpolationSyntaxError(Exception):
    """Exception raised when the source text into which substitutions
    are made does not conform to the required syntax. Subclass of
    InterpolationError."""

class MissingSectionHeaderError(Exception):
    """Exception raised when attempting to parse a file which has no
    section headers."""

class ParsingError(Exception):
    """Exception raised when errors occur attempting to parse a file."""

## The maximum depth for recursive interpolation for get() when the
## raw parameter is false. This is relevant only for the ConfigParser
## class.
MAX_INTERPOLATION_DEPTH = 10

class RawConfigParser(object):

    def __init__(self, encoding='utf8', percent_expand=False,
                 safe_set=False, dollar_expand=False,
                 case_sensitive=False):
        self.encoding = encoding
        self.percent_expand = percent_expand
        self.safe_set = safe_set
        self.dollar_expand = dollar_expand
        self.case_sensitive = case_sensitive
        self._pre_normalized_keys = {}
        self._pre_normalized_sections = {}
        self._key_file_positions = {}
        self._key_comments = {}
        self._section_order = []
        self._section_key_order = {}
        self._values = {}
        self._percent_defaults = {}

    def defaults(self):
        """Return a dictionary containing the instance-wide defaults."""
        return self._defaults

    def sections(self):
        """Return a list of the sections available; DEFAULT is not
        included in the list."""
        raise NotImplemented

    def add_section(self, section):
        """Add a section named section to the instance.

        If a section by the given name already exists,
        DuplicateSectionError is raised.
        """
        raise NotImplemented

    def has_section(self, section):
        """Indicates whether the named section is present in the
        configuration.

        The DEFAULT section is not acknowledged.
        """
        raise NotImplemented

    def options(self, section):
        """Returns a list of options available in the specified
        section."""
        raise NotImplemented

    def has_option(self, section, option):
        """If the given section exists, and contains the given option,
        return True; otherwise return False."""
        raise NotImplemented

    def read(self, filenames):
        """Attempt to read and parse a list of filenames, returning a
        list of filenames which were successfully parsed.

        If filenames is a string or Unicode string, it is treated as a
        single filename. If a file named in filenames cannot be
        opened, that file will be ignored. This is designed so that
        you can specify a list of potential configuration file
        locations (for example, the current directory, the user's home
        directory, and some system-wide directory), and all existing
        configuration files in the list will be read. If none of the
        named files exist, the ConfigParser instance will contain an
        empty dataset. An application which requires initial values to
        be loaded from a file should load the required file or files
        using readfp() before calling read() for any optional files:

          import ConfigParser, os

          config = ConfigParser.ConfigParser()
          config.readfp(open('defaults.cfg'))
          config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])
        """
        raise NotImplemented

    def readfp(self, fp, filename='<???>'):
        """Read and parse configuration data from the file or
        file-like object in fp

        Only the readline() method is used. If filename is omitted and
        fp has a name attribute, that is used for filename; the
        default is '<???>'.
        """
        raise NotImplemented

    def get(self, section, option, raw=False, vars=None):
        """Get an option value for the named section.

        If self.percent_expand is true, then all the '%'
        interpolations are expanded, using the optional vars.  If raw
        is True, then no interpolation is done."""
        raise NotImplemented

    def getint(self, section, option):
        """A convenience method which coerces the option in the
        specified section to an integer."""
        raise NotImplemented

    def getfloat(self, section, option):
        """A convenience method which coerces the option in the
        specified section to a floating point number."""
        raise NotImplemented

    def getboolean(self, section, option):
        """A convenience method which coerces the option in the
        specified section to a Boolean value.

        Note that the accepted values for the option are "1", "yes",
        "true", and "on", which cause this method to return True, and
        "0", "no", "false", and "off", which cause it to return
        False. These string values are checked in a case-insensitive
        manner. Any other value will cause it to raise ValueError.
        """
        raise NotImplemented

    def items(self, section, raw=False, vars=None):
        """Return a list of (name, value) pairs for each option in the
        given section.

        If self.percent_expand is true, then all the '%'
        interpolations are expanded, using the optional vars.  If raw
        is True, then no interpolation is done.
        """
        raise NotImplemented
        
    def set(self, section, option, value):
        """If the given section exists, set the given option to the
        specified value; otherwise raise NoSectionError.

        While it is possible to use RawConfigParser (or ConfigParser
        with raw parameters set to true) for internal storage of
        non-string values, full functionality (including interpolation
        and output to files) can only be achieved using string values.

        If self.safe_set is true, then only string values will be
        allowed.
        """
        raise NotImplemented

    def write(self, fileobject):
        """Write a representation of the configuration to the
        specified file object.

        This representation can be parsed by a future read() call.
        """
        raise NotImplemented

    def remove_option(self, section, option):
        """Remove the specified option from the specified section.

        If the section does not exist, raise NoSectionError. If the
        option existed to be removed, return True; otherwise return
        False.
        """
        raise NotImplemented

    def remove_section(self, section):
        """Remove the specified section from the configuration.

        If the section in fact existed, return True. Otherwise return
        False.
        """
        raise NotImplemented

    def optionxform(self, option):
        """Transforms the option name option as found in an input file
        or as passed in by client code to the form that should be used
        in the internal structures.

        The default implementation returns a lower-case version of
        option; subclasses may override this or client code can set an
        attribute of this name on instances to affect this
        behavior. Setting this to str(), for example, would make
        option names case sensitive.
        """
        if self.case_sensitive:
            return option.lower()
        else:
            return option
