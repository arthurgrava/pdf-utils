import fire
from PyPDF2 import PdfFileWriter, PdfFileReader


def check_if_index_might_be_out_of_bounds(reader, pages):
    num_pages = reader.getNumPages() - 1 # index starts at pos 0
    for page in pages:
        if page > num_pages:
            raise IOError(f'Max number of pages is {num_pages + 1}')


def get_pages(pages):
    if isinstance(pages, int):
        return [pages,]
    return [int(page) for page in pages]


def run(infile, pages, output_name):
    reader = PdfFileReader(infile)
    select_pages = get_pages(pages)
    check_if_index_might_be_out_of_bounds(reader, select_pages)

    outfile = PdfFileWriter()
    for page in select_pages:
        outfile.addPage(reader.getPage(page))
    with open(output_name, 'wb') as wr:
        outfile.write(wr)


if __name__ == "__main__":
    fire.Fire(run)
