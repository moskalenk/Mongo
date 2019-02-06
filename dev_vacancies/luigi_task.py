import luigi
import pymongo
from extract import Extract
import load


class ETLTask(luigi.Task):
    context = luigi.DictParameter(default=None)

    def __init__(self, context=None):
        super().__init__(context)
        self._completed = False
        self.dev_data = None
        self._client = pymongo.MongoClient()
        self._db = self._client[self.context["mongo_database"]]

    @property
    def client(self):
        return self._client

    @property
    def destination_collection(self):
        return self._db.get_collection(self.context["mongo_destination_collection"])

    def run(self):
        self._completed = True

    def complete(self):
        return self._completed


class ExtractTask(ETLTask):
    def run(self):
        self.dev_data = Extract().get_data()
        super().run()

    def output(self):
        return self.dev_data


class LoadTask(ETLTask):
    def requires(self):
        return ExtractTask(self.context)

    def run(self):
        dev_data = self.input()
        load.load_data_to_collection(dev_data, self.destination_collection)
        super().run()


class ParserTask(luigi.WrapperTask):
    mongo_database = luigi.Parameter(default="vacancies")
    mongo_destination_collection = luigi.Parameter(default="destination_collection")

    def __init__(self):
        super().__init__()
        self.context = {
            "mongo_database": self.mongo_database,
            "mongo_destination_collection": self.mongo_destination_collection
        }

    def requires(self):
        return LoadTask(self.context)


if __name__ == "__main__":
    luigi.run(
        cmdline_args=[],
        main_task_cls=ParserTask,
        local_scheduler=False)
