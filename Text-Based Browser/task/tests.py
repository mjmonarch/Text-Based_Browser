from hstest.stage_test import *
import requests
import os
import shutil
from bs4 import BeautifulSoup
import sys

if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TextBasedBrowserTest(StageTest):

    def generate(self):

        dir_for_files = os.path.join(os.curdir, 'tb_tabs')
        return [
            TestCase(
                stdin='ikea.com\nexit',
                attach='ikea.com',
                args=[dir_for_files]
            ),
            TestCase(
                stdin='en.wikipedia.org\nexit',
                attach='en.wikipedia.org',
                args=[dir_for_files]
            ),
            TestCase(
                stdin='nytimescom\nexit',
                args=[dir_for_files]
            ),
        ]

    def check_output(self, output_text: str, ideal_text: list, page_code: list, source: str):
        """
        :param output_text: the text from the user's file or from the console output
        :param ideal_text: the text from the web page (without HTML tags)
        :param page_code: the text from the web page with HTML tags
        :param source: the name of the file from which the user's text is taken or "console output" line
        :return: raises WrongAnswer if an HTML tag is found in the output_text
        or if a word from the ideal_text is not found in the output_text
        """
        for line in page_code:
            if line not in ideal_text and line in output_text:
                raise WrongAnswer(f"The following token is present in the {source} even though it's not expected to be there:\n"
                                  f"\'{line}\'\n"
                                  f"Make sure you get rid of all HTML tags.")
        output_text = ''.join(char for char in output_text if char.isalnum())
        for line in ideal_text:
            line_without_spaces = ''.join(char for char in line if char.isalnum())
            if line_without_spaces.strip() not in output_text:
                raise WrongAnswer(f"The following token is missing from the {source}:\n"
                                  f"\'{line}\'\n"
                                  f"Make sure you get all the text from the web page.")

    def _check_files(self, path_for_tabs: str, ideal_page: list, page_code: list):
        """
        Helper which checks that browser saves visited url in files and
        provides access to them.

        :param path_for_tabs: directory which must contain saved tabs
        :param ideal_page: the text from the web page (without HTML tags)
        :param page_code: the text from the web page with HTML tags
        """

        path, dirs, filenames = next(os.walk(path_for_tabs))

        for file in filenames:
            print("file: {}".format(file))
            with open(os.path.join(path_for_tabs, file), 'r', encoding='utf-8') as tab:
                try:
                    content = tab.read()
                except UnicodeDecodeError:
                    raise WrongAnswer('An error occurred while reading your saved tab. '
                                      'Perhaps you used the wrong encoding?')
                self.check_output(content, ideal_page, page_code, "file " + file)

    @staticmethod
    def get_page_and_code(url):
        """
        :param url: url link that the program is requested to open
        :return: list with strings of clean text and list of strings with text with HTML tags
        """

        url = f'https://{url}'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/70.0.3538.77 Safari/537.36"
        try:
            page = requests.get(url, headers={'User-Agent': user_agent})
        except requests.exceptions.ConnectionError:
            raise WrongAnswer(f"An error occurred while tests tried to connect to the page {url}.\n"
                              f"Please try again a bit later.")
        soup = BeautifulSoup(page.content, 'html.parser')
        tags = soup.find_all(['p', 'a', 'h1', 'h2', 'ul', 'ol', 'li'])
        text = []
        tagged_text = []
        for tag in tags:
            tag_text = tag.text.strip()
            if tag_text:
                text.append(tag_text)
            tag = str(tag)
            if tag.startswith('<'):
                tagged_text.append(tag)
        return text, tagged_text

    def check(self, reply, attach):

        # Incorrect URL
        if attach is None:
            if 'incorrect url' not in reply.lower():
                return CheckResult.wrong('An invalid URL was input to your program.\n'
                                         'Your program should print \'Incorrect URL\'.')
            else:
                return CheckResult.correct()

        # Correct URL
        if isinstance(attach, str):
            ideal_text, page_code = TextBasedBrowserTest.get_page_and_code(attach)

            path_for_tabs = os.path.join(os.curdir, 'tb_tabs')

            if not os.path.isdir(path_for_tabs):
                return CheckResult.wrong("There is no directory for tabs")

            self._check_files(path_for_tabs, ideal_text, page_code)

            try:
                shutil.rmtree(path_for_tabs)
            except PermissionError:
                return CheckResult.wrong("Impossible to remove the directory for tabs. Perhaps you haven't closed some file?")

            self.check_output(reply, ideal_text, page_code, "console output")

            return CheckResult.correct()


TextBasedBrowserTest().run_tests()
