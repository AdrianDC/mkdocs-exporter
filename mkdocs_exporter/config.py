from typing import Callable

from mkdocs.config import config_options as c
from mkdocs.config.base import Config as BaseConfig

from mkdocs_exporter.formats.pdf.config import Config as PDFFormatConfig


class FormatsConfig(BaseConfig):

  """The PDF format configuration."""
  pdf = c.SubConfig(PDFFormatConfig)


class ButtonConfig(BaseConfig):
  """The configuration of a button."""

  enabled = c.Type((bool, Callable), default=True)
  """Is the button enabled?"""

  title = c.Type((str, Callable))
  """The button's title."""

  icon = c.Type((str, Callable))
  """The button's icon (typically, an SVG element)."""

  attributes = c.Type((dict, Callable), default={})
  """Some extra attributes to add to the button."""


class Config(BaseConfig):
  """The plugin's configuration."""

  theme = c.Optional(c.Theme(default=None))
  """Override the theme used by your MkDocs instance."""

  formats = c.SubConfig(FormatsConfig)
  """The formats to generate."""

  buttons = c.ListOfItems(c.SubConfig(ButtonConfig))
  """The buttons to add."""
