from ir.documents import TextDocument
from .Demo import Demo
import webbrowser
import os


class ConsoleDemo(Demo):
    def start(self):
        while True:
            query = input("Query: ")

            if query == "":
                break

            retrievals = self.inverted_index.retrieve(TextDocument(query, pipeline=self.pipeline))
            self.present_retrievals(retrievals)

    def open_in_browser(self, doc):
        path = "file://" + os.path.realpath(os.path.join(self.collection.dir_path, doc.file_name))
        webbrowser.open(path, new=0, autoraise=True)

    @staticmethod
    def print_retrievals(retrievals, start, size):
        for i in range(start, min(start + size, len(retrievals))):
            doc, score = retrievals[i]
            print(f"{i + 1}: {doc.file_name}       ({score})")

    def process_retrieval_command(self, retrievals):
        c = input("\t Command: ")
        if c == "":
            return -1
        elif c == "m":
            return 1

        try:
            n = int(c)
            if n < 1 or n > len(retrievals):
                raise Exception
        except Exception:
            self.print_subcommand_usage(retrievals)
            return 0

        self.open_in_browser(retrievals[n - 1][0])
        return 0

    @staticmethod
    def print_subcommand_usage(retrievals):
        print(f"\nEnter 'm' to view more, press [ENTER] to return or enter a number from {1} to {len(retrievals)}\n")

    def present_retrievals(self, retrievals):
        retrievals = list(retrievals)
        size = 10
        start = 0

        if len(retrievals) == 0:
            print("No documents found :(")
            return

        self.print_retrievals(retrievals, start, size)

        self.print_subcommand_usage(retrievals)

        while True:
            res = self.process_retrieval_command(retrievals)
            if res == -1:
                break
            elif res == 1:
                start += size
                self.print_retrievals(retrievals, start, size)
