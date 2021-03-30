import fire as fire

from pet_store.entrypoints import cli

if __name__ == '__main__':
    fire.Fire(cli.cli)
