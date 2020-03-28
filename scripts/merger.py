import fire
from PyPDF2 import PdfFileWriter, PdfFileReader


def get_readers(value):
    names = value.split(',')
    return [PdfFileReader(name) for name in names]

def run(output_name, merge_these):
    readers = get_readers(merge_these)

    outfile = PdfFileWriter()
    for reader in readers:
        pages = reader.getNumPages()
        for i in range(0, pages):
            outfile.addPage(
                reader.getPage(i)
            )

    with open(output_name, 'wb') as wr:
        outfile.write(wr)


if __name__ == "__main__":
    fire.Fire(run)
