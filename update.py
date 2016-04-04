from cltk_capitains_corpora_converter import run

def update():
    run(
        "cloned",
        output="json",
        repository="https://github.com/OpenGreekAndLatin/csel-dev.git",
        nodes=["tei:note", "tei:orig"],
        credit="Open Philology, Humboldt Chair of Digital Humanities ( https://github.com/OpenGreekAndLatin/csel-dev )",
        silent=False
    )

if __name__ == '__main__':
    update()