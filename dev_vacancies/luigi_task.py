import luigi
from extract import Extract


class ExtractTask(luigi.Task):
    def run(self):
        res = Extract().get_data()
        with self.output().open('w') as f:
            f.write(res)

    def output(self):
        return luigi.LocalTarget('result.txt')


class LoadTask(luigi.Task):
    def requires(self):
        return ExtractTask()

    def run(self):
        with self.input().open('r') as f:
            print(f.read())


if __name__ == "__main__":
    luigi.run(
        cmdline_args=[],
        main_task_cls=ExtractTask,
        local_scheduler=False)
