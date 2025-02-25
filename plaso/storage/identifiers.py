# -*- coding: utf-8 -*-
"""Storage attribute container identifier objects."""

from plaso.containers import interface as containers_interface


class FakeIdentifier(containers_interface.AttributeContainerIdentifier):
  """Fake attribute container identifier intended for testing.

  Attributes:
    name (str): name of the attribute container.
    sequence_number (int): sequence number of the attribute container.
  """

  def __init__(self, name, sequence_number):
    """Initializes a fake attribute container identifier.

    Args:
      name (str): name of the table.
      sequence_number (int): sequence number of the attribute container.
    """
    super(FakeIdentifier, self).__init__()
    self.name = name
    self.sequence_number = sequence_number

  def CopyToString(self):
    """Copies the identifier to a string representation.

    Returns:
      str: unique identifier or None.
    """
    if self.name is not None and self.sequence_number is not None:
      return '{0:s}.{1:d}'.format(self.name, self.sequence_number)

    return None


class RedisKeyIdentifier(containers_interface.AttributeContainerIdentifier):
  """Redis key attribute container identifier.

  Attributes:
    name (str): name of the attribute container.
    sequence_number (int): sequence number of the attribute container.
  """

  def __init__(self, name, sequence_number):
    """"Initializes a Redis key identifier.

    Args:
      name (str): name of the table.
      sequence_number (int): sequence number of the attribute container.
    """
    super(RedisKeyIdentifier, self).__init__()
    self.name = name
    self.sequence_number = sequence_number

  def CopyToString(self):
    """Copies the identifier to a string representation.

    Returns:
      str: unique identifier or None.
    """
    if self.name is not None and self.sequence_number is not None:
      return '{0:s}.{1:d}'.format(self.name, self.sequence_number)

    return None


class SQLTableIdentifier(containers_interface.AttributeContainerIdentifier):
  """SQL table attribute container identifier.

  The identifier is used to uniquely identify attribute containers. Where
  for example an attribute container is stored as a JSON serialized data in
  a SQLite database file.

  Attributes:
    name (str): name of the table (attribute container).
    sequence_number (int): sequence number of the attribute container.
  """

  def __init__(self, name=None, sequence_number=None):
    """Initializes a SQL table attribute container identifier.

    Args:
      name (Optional[str]): name of the table (attribute container).
      sequence_number (Optional[int]): sequence number of the attribute
          container.
    """
    super(SQLTableIdentifier, self).__init__()
    self.name = name
    self.sequence_number = sequence_number

  def CopyFromString(self, identifier_string):
    """Copies the identifier from a string representation.

    Args:
      identifier_string (str): string representation.
    """
    self.name, sequence_number = identifier_string.split('.')
    self.sequence_number = int(sequence_number, 10)

  def CopyToString(self):
    """Copies the identifier to a string representation.

    Returns:
      str: unique identifier or None.
    """
    if self.name is not None and self.sequence_number is not None:
      return '{0:s}.{1:d}'.format(self.name, self.sequence_number)

    return None
