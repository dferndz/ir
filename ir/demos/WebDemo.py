from .Demo import Demo
from argparse import ArgumentParser


class WebDemo(Demo):
    def start(self):
        from .flask_app.app import app

        app.config["inverted_index"] = self.inverted_index
        app.config["pipeline"] = self.pipeline
        app.config["collection"] = self.collection
        app.run(debug=self.args.debug, use_reloader=self.args.debug)

    def prepare_parser(self, parser: ArgumentParser):
        parser.add_argument(
            "--debug",
            required=False,
            default=False,
            action="store_true",
            help="For debugging",
        )
