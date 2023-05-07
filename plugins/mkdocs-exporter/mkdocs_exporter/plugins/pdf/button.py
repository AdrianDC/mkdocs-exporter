import os

from textwrap import dedent
from mkdocs_exporter.page import Page


def href(page: Page) -> str:
  """The button's 'href' attribute."""

  return os.path.relpath(page.formats['pdf'], page.url)


def download(page: Page) -> str:
  """The button's 'download' attribute."""

  return page.title + os.path.extsep + 'pdf'


def icon(page: Page) -> str:
  """The button's icon."""

  return dedent('''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
      <path d="m14 2 6 6v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8m4 18V9h-5V4H6v16h12m-6-1-4-4h2.5v-3h3v3H16l-4 4Z"/>
    </svg>
  ''')
