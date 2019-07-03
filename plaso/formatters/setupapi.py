# -*- coding: utf-8 -*-
"""Windows Setupapi log event formatter."""

from __future__ import unicode_literals

from plaso.formatters import interface
from plaso.formatters import manager


class SetupapiLogFormatter(interface.ConditionalEventFormatter):
  """Formatter for a Windows Setupapi log file event."""

  DATA_TYPE = 'setupapi:log:line'

  FORMAT_STRING_PIECES = [
      'Description: {entry_type} |',
      'Exit status: {exit_status}']

  FORMAT_STRING_SHORT_PIECES = ['{entry_type}']

  SOURCE_LONG = 'Windows Setupapi Log'
  SOURCE_SHORT = 'LOG'


manager.FormattersManager.RegisterFormatter(SetupapiLogFormatter)